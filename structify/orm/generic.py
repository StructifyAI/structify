from pydantic import BaseModel


class GenericResponse(BaseModel):
    """
    A basic response from the API.
    """

    success: bool
    message: str
