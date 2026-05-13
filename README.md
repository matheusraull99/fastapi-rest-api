# FastAPI REST API — Gerenciador de Tarefas

API REST completa com FastAPI, SQLAlchemy e SQLite. CRUD completo de tarefas com documentação interativa automática.

## Tecnologias

- Python 3.11+
- FastAPI 0.111
- SQLAlchemy 2.0 (ORM)
- Pydantic v2 (validação)
- SQLite (banco de dados)
- Uvicorn (servidor ASGI)

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

```bash
cp .env.example .env
```

## Executar

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa em:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/tarefas` | Lista todas as tarefas |
| `POST` | `/tarefas` | Cria nova tarefa |
| `GET` | `/tarefas/{id}` | Busca tarefa por ID |
| `PATCH` | `/tarefas/{id}` | Atualiza tarefa |
| `DELETE` | `/tarefas/{id}` | Remove tarefa |

### Filtros disponíveis em `GET /tarefas`

- `?concluida=true` — apenas concluídas
- `?concluida=false` — apenas pendentes
- `?skip=0&limit=10` — paginação

## Exemplo de uso

```bash
# Criar tarefa
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Estudar FastAPI", "descricao": "Ver documentação oficial"}'

# Listar tarefas pendentes
curl http://localhost:8000/tarefas?concluida=false

# Concluir tarefa
curl -X PATCH http://localhost:8000/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"concluida": true}'
```

## Estrutura

```
fastapi-rest-api/
├── main.py         # Rotas e aplicação FastAPI
├── models.py       # Modelos do banco de dados (SQLAlchemy)
├── schemas.py      # Schemas de validação (Pydantic)
├── database.py     # Configuração do banco de dados
├── requirements.txt
└── .env.example
```
