from pydantic import BaseModel


class KnowledgeGraph(BaseModel):
    """
    A local knowledge graph representation. This isn't meant to
    be a knowledge graph itself, but raather a pointer to one
    on the server.
    """

    pass
