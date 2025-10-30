from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import encuesta, estadistica

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Podés usar ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Permite cualquier header
)

# Incluir el router de encuestas
app.include_router(encuesta.router)
app.include_router(estadistica.router)