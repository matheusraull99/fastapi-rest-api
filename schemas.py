from pydantic import BaseModel, Field
from datetime import datetime


class TarefaCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200, examples=["Estudar FastAPI"])
    descricao: str | None = Field(None, examples=["Ver documentação oficial"])


class TarefaUpdate(BaseModel):
    titulo: str | None = Field(None, min_length=1, max_length=200)
    descricao: str | None = None
    concluida: bool | None = None


class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: str | None
    concluida: bool
    criado_em: datetime
    atualizado_em: datetime

    model_config = {"from_attributes": True}
