import torch
import os
from transformers.tools import LocalAgent
from transformers import AutoModelForCausalLM, AutoTokenizer
import structify

username = os.environ.get("STRUCTIFY_USERNAME")
password = os.environ.get("STRUCTIFY_PASSWORD")
structify.login(username, password)

checkpoint = "meta-llama/Llama-2-13b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


agent = LocalAgent(model, tokenizer, additional_tools=[structify.StructifyData()])
agent.run("List all businesses from the structify db using a query.")
