from transformers import Tool
from huggingface_hub import list_models
from PIL import Image
import requests


class StructifyData(Tool):
    name = "structify_data"
    description = (
        "This tool facilitates interaction with a business-oriented knowledge graph which encapsulates data on companies and persons. Utilizing Cypher queries, you can retrieve specific data points from the graph database. The knowledge graph comprises of two main entities: 'Company' and 'Person'. A 'Company' entity possesses attributes such as 'Name', 'Address', 'CIK', 'Rounds', and 'Employees', while a 'Person' entity contains an attribute 'Person Name'. A Cypher query can be crafted to fetch data based on these attributes or relationships among these entities.\n"
        "\n"
        "Example 1: To retrieve the name and address of a company:\n"
        "Cypher Query: 'MATCH (c:Company) RETURN c.Name, c.Address'\n"
        "\n"
        "Example 2: To obtain the names of all employees working in a particular company:\n"
        "Cypher Query: 'MATCH (c:Company)-[:HAS]->(e:Person) WHERE c.Name = 'Target Company' RETURN e.PersonName'\n"
        "\n"
        "Feed a Cypher query through the 'query' input parameter to extract desired data. The resultant data is fetched from the endpoint 'http://localhost:8000/api/kg/query'."
        "And the tool syntax is output=structify_data('{query}'). Save the output to a file called \"test.txt\" when you've gotten results."
    )
    inputs = ["query"]
    outputs = ["image"]

    def __call__(self, query):
        query = "MATCH (n) RETURN n;"
        result = requests.get("http://localhost:8000/api/agent/query", params={"query": query})
        return result.text
        
