import structify
from transformers.tools import HfAgent

structify.login("username", "password")

agent = HfAgent(
    "https://api-inference.huggingface.co/models/bigcode/starcoder", additional_tools=[structify.StructifyData()]
)
agent.run(
    (
        "Find all businesses who have YC as an investor and raised a later round of over 10 million."
        "Save the company's names in a file called deals.csv."
    )
)
