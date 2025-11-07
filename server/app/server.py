from fastapi import FastAPI, Request, HTTPException
import json
import uvicorn
import os

app = FastAPI()
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_RAIZ = os.path.abspath(os.path.join(DIRETORIO_ATUAL, os.pardir, os.pardir))
CAMINHO_JSON = os.path.join(CAMINHO_RAIZ, 'server', 'dados', 'champions.json')
archive_name = CAMINHO_JSON

def open_bd():
    try:
        with open(archive_name, 'r', encoding='utf-8') as archive:
            return json.load(archive)
    except FileNotFoundError:
        print(f'Erro: O arquivo {archive_name} não foi encontrado')
    except json.JSONDecodeError:
        print(f'O arquivo JSON é inválido.')
    except Exception as e:
        print(f'Ocorreu um: {e}')
    #return champ

def write_bd(champ):
    try:
        with open(archive_name, 'w', encoding='utf-8') as archive:
            json.dump(champ, archive, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(f'Erro: O arquivo {archive_name} não foi encontrado')
    except json.JSONDecodeError:
        print(f'O arquivo JSON é inválido.')
    except Exception as e:
        print(f'Ocorreu um: {e}')

@app.get('/champion/all')
def get_all():
    champ = open_bd()
    return champ['data']

@app.get('/champion/{name}/build{id}')
def get_build_champ(name: str, id: int):
    champ = open_bd()
    if name not in champ['data']:
        raise HTTPException(status_code=400, detail='Esse campeão não existe.')
    return champ['data'][name]['build'][id-1]

@app.get('/champion/{name}')
def get_champ(name: str):
    champ = open_bd()
    if name not in champ['data']:
        raise HTTPException(status_code=400, detail='Esse campeão não existe.')
    return champ['data'].get(name)

@app.post('/champion/{name}/build')
async def insert_build(name: str, request: Request):
    champ = open_bd()
    
    items = await request.json()

    if not 'build' in champ['data'][name]:
        champ['data'][name]['build'] = []

    new_build = {
        'id': len(champ['data'][name]['build'])+1,
        'item1': items['item1'],
        'item2': items['item2'],
        'item3': items['item3'],
        'item4': items['item4'],
        'item5': items['item5'],
        'item6': items['item6'],
    }
    champ['data'][name]['build'].append(new_build)
    write_bd(champ)
    return {"message": "Build inserida com sucesso!", "build": new_build}

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True)