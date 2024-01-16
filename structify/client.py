import json
import logging
from inspect import isfunction
from types import SimpleNamespace
from typing import Any, List, Optional
import requests
from pydantic import BaseModel
from structify.endpoint import ENDPOINT
from structify.orm import Document, GenericResponse, KnowledgeGraph, Schema


class QueryBuilder:
    ENDPOINTS = {
        "/agent/scrape": ("POST", None),
        "/documents/add": ("POST", Document),
        "/documents/delete": ("DELETE", Document),
        "/entities/add": ("POST", GenericResponse),
        "/kg/add": ("POST", GenericResponse),
        "/kg/create": ("POST", GenericResponse),
        "/kg/delete": ("POST", GenericResponse),
        "/kg/get": ("POST", KnowledgeGraph),
        "/researcher/crawl": ("POST", lambda x: [SimpleNamespace(**z) for z in x]),
        "/schemas/add": ("POST", GenericResponse),
        "/schemas/delete": ("POST", Schema),
        "/schemas/get": ("GET", Schema),
        "/schemas/list": ("GET", lambda x: [Schema(**z) for z in x]),
    }

    def __init__(self, query_parts: List[str], token: str) -> "QueryBuilder":
        self.query_parts = query_parts
        self.token = token

    def __getattr__(self, key: str) -> "QueryBuilder":
        return QueryBuilder(self.query_parts + [key], self.token)

    def __call__(self, *args, **kwargs) -> Any:
        subdomain = "/" + "/".join(self.query_parts)
        method, output = self.ENDPOINTS[subdomain]
        url = f"{ENDPOINT}{subdomain}"

        request_args = kwargs

        for arg in args:
            if hasattr(arg, "to_dict"):
                request_args.update(arg.to_dict())
            elif isinstance(arg, BaseModel):
                request_args.update(arg.model_dump())
            else:
                raise NotImplementedError(f"Unknown argument type {type(arg)}")

        for key, value in request_args.items():
            if hasattr(value, "to_dict"):
                request_args[key] = value.to_dict()

        headers = {
            "authorization": f"{self.token}",
            "Content-Type": "application/json",
        }
        if method == "POST":
            result = requests.post(url, json=request_args, headers=headers)
        elif method == "GET":
            result = requests.get(url, params=request_args, headers=headers)
        elif method == "DELETE":
            result = requests.delete(url, params=request_args, headers=headers)
        else:
            raise NotImplementedError(f"Unknown method {method}")

        res = result.json()
        if "error" in res:
            logging.warn(res["error"])
            return None

        if output is None:
            return res
        elif isfunction(output):
            return output(res)
        elif issubclass(output, BaseModel):
            return output(**res)
        else:
            return output(res)


class Client:
    def __init__(self, auth: str) -> "Client":
        self.token = auth

    def scrape(self, query: str, output: Optional[BaseModel] = None) -> BaseModel:
        schema = output.model_json_schema()
        payload = json.dumps({"query": query, "schema": json.dumps(schema)})
        result = requests.post(
            f"{ENDPOINT}/agent/scrape",
            data=payload,
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return output(**json.loads(result.json()))

    def __getattr__(self, key: str):
        return QueryBuilder([key], self.token)


def login(email: str, password: str) -> Client:
    global AUTH_TOKEN
    result = requests.post(f"{ENDPOINT}/auth/login/", json={"email": email, "password": password})
    AUTH_TOKEN = result.json()["token"]
    return AUTH_TOKEN
