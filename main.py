from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Dict, Optional

LISTA_TAREFAS = []
APP = FastAPI()

def nova_tarefa(id: int, titulo: str, descricao: str):
    """Função auxiliar para criar uma tarefa usando dicionário"""
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now().isoformat()
    }

@APP.get("/")
def index():
    return "Olá, DevOps!"

@APP.get("/tarefas")
def listar_tarefas():
    """Lista tarefas (somente id e titulo)"""
    if not LISTA_TAREFAS:
        return []
    
    return [{"id": t["id"], "titulo": t["titulo"]} for t in LISTA_TAREFAS]

@APP.get("/tarefas/{id}")
def listar_tarefa_especifica(id: int):
    """Retorna uma tarefa específica pelo índice"""
    if not LISTA_TAREFAS:
        return {"mensagem": "Não existe nenhuma tarefa"}
    
    if 0 <= id < len(LISTA_TAREFAS):
        return LISTA_TAREFAS[id]
    
    return {"mensagem": "Não existe nenhuma tarefa"}

# ==================== ROTAS A IMPLEMENTAR ====================

@APP.post("/tarefas")
def criar_tarefa(titulo: str, descricao: str):
    """Cria uma nova tarefa"""
    if not titulo or not descricao:
        raise HTTPException(status_code=400, detail="Título e descrição são obrigatórios")
    
    novo_id = len(LISTA_TAREFAS)
    tarefa = nova_tarefa(novo_id, titulo, descricao)
    LISTA_TAREFAS.append(tarefa)
    
    return {
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": tarefa
    }

@APP.put("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: Optional[str] = None, descricao: Optional[str] = None, concluido: Optional[bool] = None):
    """Atualiza uma tarefa existente (pode atualizar campos específicos)"""
    if not LISTA_TAREFAS:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada")
    
    if id < 0 or id >= len(LISTA_TAREFAS):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    tarefa = LISTA_TAREFAS[id]
    
    if titulo is not None:
        tarefa["titulo"] = titulo
    if descricao is not None:
        tarefa["descricao"] = descricao
    if concluido is not None:
        tarefa["concluido"] = concluido
    
    return {
        "mensagem": "Tarefa atualizada com sucesso",
        "tarefa": tarefa
    }

@APP.delete("/tarefas")
def deletar_todas_tarefas():
    """Deleta todas as tarefas"""
    global LISTA_TAREFAS
    quantidade = len(LISTA_TAREFAS)
    LISTA_TAREFAS.clear()
    
    return {
        "mensagem": f"{quantidade} tarefa(s) deletada(s) com sucesso",
        "total_restante": len(LISTA_TAREFAS)
    }