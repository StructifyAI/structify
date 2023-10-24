import torch
from transformers.tools import LocalAgent
from transformers import AutoModelForCausalLM, AutoTokenizer
import structify

structify.login("alex@structify.ai", "123WestSt")

checkpoint = "meta-llama/Llama-2-13b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


agent = LocalAgent(model, tokenizer, additional_tools=[structify.StructifyData()])
agent.run("List all businesses from the structify db using a query.")
