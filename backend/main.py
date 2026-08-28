import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from engine import analisar_colaborador

DATA_PATH = Path(__file__).parent / "data.json"

app = FastAPI(title="Cuida AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def carregar_colaboradores() -> list[dict]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["colaboradores"]


def buscar_colaborador(colab_id: str) -> dict:
    colab = next((c for c in carregar_colaboradores() if c["id"] == colab_id), None)
    if colab is None:
        raise HTTPException(status_code=404, detail="Colaborador não encontrado")
    return colab


@app.get("/api/colaboradores")
def listar_colaboradores():
    return carregar_colaboradores()


@app.post("/api/colaboradores/{colab_id}/diagnostico")
def gerar_diagnostico(colab_id: str):
    colab = buscar_colaborador(colab_id)
    return analisar_colaborador(colab)
