from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Tarefa
from schemas import TarefaCreate, TarefaUpdate, TarefaResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Tarefas",
    description="API REST completa para gerenciamento de tarefas com FastAPI + SQLite",
    version="1.0.0",
)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "API de Tarefas funcionando!"}


@app.get("/tarefas", response_model=list[TarefaResponse], tags=["Tarefas"])
def listar_tarefas(
    concluida: bool | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    query = db.query(Tarefa)
    if concluida is not None:
        query = query.filter(Tarefa.concluida == concluida)
    return query.offset(skip).limit(limit).all()


@app.post("/tarefas", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED, tags=["Tarefas"])
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    nova = Tarefa(**tarefa.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@app.get("/tarefas/{tarefa_id}", response_model=TarefaResponse, tags=["Tarefas"])
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@app.patch("/tarefas/{tarefa_id}", response_model=TarefaResponse, tags=["Tarefas"])
def atualizar_tarefa(tarefa_id: int, dados: TarefaUpdate, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(tarefa, campo, valor)
    db.commit()
    db.refresh(tarefa)
    return tarefa


@app.delete("/tarefas/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tarefas"])
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
