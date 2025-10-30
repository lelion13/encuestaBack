from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
import sqlite3

app = FastAPI()

# Inicializar la base de datos
def init_db():
    conn = sqlite3.connect("encuestas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo TEXT NOT NULL,
            valor INTEGER NOT NULL,
            fecha_hora TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Modelo de datos que se recibe
class Encuesta(BaseModel):
    equipo: str
    valor: int  # Ej: 1 = 😡, 2 = 😐, 3 = 🙂, 4 = 😀

@app.post("/encuesta")
async def registrar_encuesta(encuesta: Encuesta):
    fecha_hora = datetime.now().isoformat()
    conn = sqlite3.connect("encuestas.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO encuestas (equipo, valor, fecha_hora)
        VALUES (?, ?, ?)
    """, (encuesta.equipo, encuesta.valor, fecha_hora))
    conn.commit()
    conn.close()
    return {"mensaje": "Encuesta registrada", "fecha_hora": fecha_hora}