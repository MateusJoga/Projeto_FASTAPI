from fastapi import FastAPI
import json
import uvicorn
from pathlib import Path
import os

app = FastAPI()
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_RAIZ = os.path.abspath(os.path.join(DIRETORIO_ATUAL, os.pardir, os.pardir))
CAMINHO_JSON = os.path.join(CAMINHO_RAIZ, 'server', 'dados', 'champions.json')
CAMINHO_BUILD = os.path.join(CAMINHO_RAIZ, 'server', 'dados', 'builds.json')
archive_name = CAMINHO_JSON
build_name = CAMINHO_BUILD

try:
    with open(archive_name, 'r', encoding='utf-8') as archive:
        champ = json.load(archive)
    with open(build_name, 'r', encoding='utf-8') as archive:
        build = json.load(archive)
except FileNotFoundError:
    print(f'Erro: O arquivo {archive_name} não foi encontrado')
except json.JSONDecodeError:
    print(f'O arquivo JSON é inválido.')
except Exception as e:
    print(f'Ocorreu um: {e}')

@app.get('/champion/all')
def get_all():
    return champ['data']

@app.get('/champion/{name}')
def get_champ(name):
    return champ['data'][name]

@app.post('/champion/{name}/build')
def insert_build(name):



if __name__ == '__main__':
    uvicorn.run('server:app', reload=True)