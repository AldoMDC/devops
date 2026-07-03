from fastapi import FastAPI
from datetime import datetime

LISTA_TAREFAS = []
APP = FastAPI()


def nova_tarefa(id: int, titulo: str, descricao: str):
    """Função auxiliar para criar uma tarefa usando dicionário (`dict`)"""
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now()
    }


@APP.get("/")
def index():
    return "Olá, DevOps!"


@APP.get("/tarefas")
def listar_tarefas():
    # Lista tarefas (somente id e titulo)
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS

    tarefas = []
    for tarefa in LISTA_TAREFAS:
        info = {"id": tarefa['id'], "titulo": tarefa['titulo']}
        tarefas.append(info)

    return tarefas


@APP.get("/tarefas/{id}")
def listar_tarefa_especifica(id: int):
    mensagem_padrao = {"mensagem": "Não existe nenhuma tarefa"}
    if len(LISTA_TAREFAS) == 0:
        return mensagem_padrao
    
    # ID da tarefa é o índice na lista
    if id >= 0 and id < len(LISTA_TAREFAS):
        return LISTA_TAREFAS[id]
    
    return mensagem_padrao


# ==================== ROTAS IMPLEMENTADAS ====================

@APP.post("/tarefas")
def criar_tarefa(id: int, titulo: str, descricao: str):
    """Rota POST /tarefas"""
    # Verifica se já existe tarefa com o mesmo ID
    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id:
            return "TAREFA JÁ EXISTE"
    
    # Cria e adiciona a nova tarefa
    tarefa = nova_tarefa(id, titulo, descricao)
    LISTA_TAREFAS.append(tarefa)
    
    return "OK"


@APP.put("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: str, descricao: str, concluido: bool):
    """Rota PUT /tarefas/{id}"""
    # Busca a tarefa pelo ID
    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id:
            # Atualiza os campos
            tarefa["titulo"] = titulo
            tarefa["descricao"] = descricao
            tarefa["concluido"] = concluido
            return "OK"
    
    return "TAREFA NÃO EXISTE"


@APP.delete("/tarefas")
def deletar_tarefa(id: int):
    """Rota DELETE /tarefas (recebe id como parâmetro)"""
    for indice, tarefa in enumerate(LISTA_TAREFAS):
        if tarefa["id"] == id:
            del LISTA_TAREFAS[indice]
            return "OK"
    
    return "TAREFA NÃO EXISTE"