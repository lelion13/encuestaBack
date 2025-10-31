from fastapi import APIRouter
import sqlite3
from collections import defaultdict

router = APIRouter()

@router.get("/estadisticas")
async def obtener_estadisticas():
    conn = sqlite3.connect("encuestas.db")
    cursor = conn.cursor()

    # Total de encuestas
    cursor.execute("SELECT COUNT(*) FROM encuestas")
    total = cursor.fetchone()[0]

    # Cantidad por valor (carita)
    cursor.execute("SELECT valor, COUNT(*) FROM encuestas GROUP BY valor")
    por_valor = {row[0]: row[1] for row in cursor.fetchall()}

    # Cantidad por equipo
    cursor.execute("SELECT equipo, COUNT(*) FROM encuestas GROUP BY equipo")
    por_equipo = {row[0]: row[1] for row in cursor.fetchall()}

    # Cantidad por día
    cursor.execute("SELECT substr(fecha_hora, 1, 10) as dia, COUNT(*) FROM encuestas GROUP BY dia")
    por_dia = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()

    return {
        "total": total,
        "por_valor": por_valor,
        "por_equipo": por_equipo,
        "por_dia": por_dia
    }