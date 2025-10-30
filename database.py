import sqlite3
from datetime import datetime

def guardar_encuesta(encuesta):
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