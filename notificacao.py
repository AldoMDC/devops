from fastapi import FastAPI
from datetime import datetime

APP_NOTIFICACAO = FastAPI()


@APP_NOTIFICACAO.post("/notificar")
def notificar_tarefa_finalizada(titulo: str, data_finalizacao: str):
    """
    Recebe o título da tarefa e a data de finalização
    e imprime uma notificação no terminal.
    """
    try:
        # Tenta formatar a data para validar
        data_formatada = datetime.fromisoformat(data_finalizacao.replace("Z", "+00:00"))
        data_legivel = data_formatada.strftime("%d/%m/%Y %H:%M:%S")
    except:
        data_legivel = data_finalizacao  # Se não conseguir formatar, usa como veio

    print("=" * 50)
    print("🔔 NOTIFICAÇÃO DE TAREFA FINALIZADA")
    print("=" * 50)
    print(f"Título da tarefa: {titulo}")
    print(f"Finalizada em:   {data_legivel}")
    print("=" * 50)
    print()

    return {
        "status": "notificação recebida",
        "titulo": titulo,
        "data_finalizacao": data_legivel
    }