# devops

## Descrição da Aplicação

API REST de **Lista de Tarefas** desenvolvida com FastAPI para a disciplina de Extensão DevOps (PUC-PR).

A aplicação permite:
- Criar, listar, atualizar e remover tarefas
- Coletar métricas (quantidade de tarefas, tempo médio de conclusão etc.)
- Health check e logging estruturado
- Documentação automática via Swagger UI (`/docs`)
  
## Tecnologias Utilizadas

- **Linguagem / Framework**: Python 3.12 + FastAPI
- **Testes**: pytest, pytest-cov, httpx
- **Qualidade**: bandit (segurança), pylint (lint)
- **Containerização**: Docker + Docker Compose
- **Proxy**: Nginx- **CI/CD**: GitHub Actions
- **Orquestração / Implantação**: Kubernetes (kubectl)
- **Registry**: Docker Hub

## Execução Local

### Pré-requisitos
- Python 3.12+
- Docker e Docker Compose (opcional, mas recomendado)

### Opção 1 – Direto com FastAPI
```bash
pip install -r requirements.txt
fastapi run app/main.py
# Acesse: http://localhost:8000/docs
```
### Opção 2 – Docker Compose
```bash
docker compose up --build
# Gateway disponível na porta 80
```
### Testes
```bash
pytest
pytest --cov --cov-fail-under=80
```
## Pipeline CI/CD
O workflow `.github/workflows/ci_cd.yaml` é acionado em:
- Pull Requests para a branch `main`
- Disparo manual (workflow_dispatch)

Fluxo: Integração -> FOSSA -> Entrega (Docker build/push) -> Implantação (Kubernetes)
