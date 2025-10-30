from fastapi import APIRouter
from models import Encuesta
from database import guardar_encuesta

router = APIRouter()

@router.post("/encuesta")
async def registrar_encuesta(encuesta: Encuesta):
    return guardar_encuesta(encuesta)