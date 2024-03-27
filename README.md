# Structify
[Screenshot](assets/logo.png)

## Getting started

### Installating the package

```bash
pip install structify.ai
```

```python
# First, define the schema of your dataset as a pydantic model
class Person(BaseModel):
    name: str
    job_title: str
    company: str

# Next, create a dataset with that schema
structify.dataset.create(name = "my_network", tables = [Person.schema()])

# Then, create an agent to index information from defined sources for your dataset
structify.agents.create(name = "my_network", source = [Source.Internet(websites = ["linkedin.com"]), Source.Document(path = "contact_cards/*")])

# Finally, let our agents structify those sources into a dataset for you
structify.it("my_network")
```