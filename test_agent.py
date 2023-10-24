import torch
from transformers.tools import LocalAgent
from transformers import AutoModelForCausalLM, AutoTokenizer
from structify import StructifyData

checkpoint = "THUDM/agentlm-13b"
model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

agent = LocalAgent(model, tokenizer, additional_tools=[StructifyData()])
agent.run("List all businesses from the structify db using a query.")
