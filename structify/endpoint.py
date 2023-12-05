import os

ENDPOINT = (
    os.environ["STRUCTIFY_ENDPOINT"]
    if "STRUCTIFY_ENDPOINT" in os.environ
    else "https://api.structify.ai"
)
