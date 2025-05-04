from contextlib import asynccontextmanager

from fastapi import FastAPI
from uvicorn import run

from fastapi.responses import RedirectResponse
from aplicacao.routes import router
from fastapi.middleware.cors import CORSMiddleware
from aplicacao.config import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('INFO: Iniciando aplicação')
    await database.create_database_tables()
    print('INFO: Tabelas criadas')
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["documentacao"])
async def index():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)