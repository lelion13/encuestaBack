from pydantic import BaseModel

class Encuesta(BaseModel):
    equipo: str
    valor: int