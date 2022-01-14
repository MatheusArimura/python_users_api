# Sobre o projeto:

O projeto foi construído utilizando o package "FastAPI", tendo tratamentos de regras de negócio dentro de uma das rotas. Não foi implementado sistema de segurança para que possam haver testes externos.

## Como executar esse código:

Será necessário instalar as dependências do código, deixadas no arquivo "requirements.txt". Pode ser feita utilizando pip no terminal, da seguinte maneira:

```bash
pip install -r requirements.txt
```

Depois de feita a instalação, deverá ser executado o comando:

```bash
uvicorn main:app --reload
```