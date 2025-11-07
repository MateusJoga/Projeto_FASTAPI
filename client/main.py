#from requests import HTTPError
import requests
import json

base_url = 'http://127.0.0.1:8000'

def listar_todos():
    endpoint = '/champion/all'
    url = base_url + endpoint
    try:
        res = requests.get(url)
        res.raise_for_status()
        dicionario = res.json()
        for champ, info in dicionario.items():
            print(f'{champ} - {info}')
    except Exception as e:
        print(f'Erro: {e}')

def validar_campeao(nome):
    endpoint = f'/champion/{nome}'
    url = base_url + endpoint
    try:
        res = requests.get(url)
        res.raise_for_status()
        champ = res.json()
        return champ
    except requests.HTTPError as http:
        error_data = res.json()
        message_error = error_data.get('detail', 'Detalhe não relatado.')
        print(f'ERRO: {message_error}')
    except Exception as e:
        print(f'ERROR: {e}')

def pesquisar_campeao(nome):
    champ = validar_campeao(nome)
    if not champ is None:
        print(f'Campeão: {champ["id"]}\nDescrição: {champ["title"]}')
    else:
        pass

def visualizar_build(nome, id):
    endpoint = f'/champion/{nome}/build{id}'
    url = base_url + endpoint
    try:
        res = requests.get(url)
        res.raise_for_status()
        build = res.json()
        for i,itens in enumerate(build.values()):
            if i == 0:
                pass
            else:
                print(f'{i}° item: {build.get("item" + str(i))}')
    except requests.HTTPError as http:
        error_data = res.json()
        message_error = error_data.get('detail', 'Detalhe não relatado.')
        print(f'ERRO: {message_error}')
    except Exception as e:
        print(f'ERROR: {e}')

def build(nome, items):
    endpoint = f'/champion/{nome}/build'
    url = base_url + endpoint
    print(f"\n--- Enviando POST para: {url} com dados: {items} ---")
    res = None
    try:
        res = requests.post(url, json=items)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ou receber resposta do servidor: {e}")
        if res is not None:
             print("Resposta de Erro: ", res.text)

def armazenar_itens():
    items = {}
    for i in range(1,7):
        items[f'item{i}'] = input(f'Digite o nome do {i}° item: ')
    return items

def menu():
    print('='*50)
    print('|X|X|X| CAMPEÕES DO LEAGUE OF LEGENDS |X|X|X|')
    print('1-Listar todos os campeões')
    print('2-Listar um campeão')
    print('3-Inserir build em um campeão')
    print('4-Pesquisar build por campeão')
    print('0-Sair')
    
if __name__ == "__main__":

    while True:
        menu()
        escolha = str(input('Escolha um número: '))
        if escolha == '1':
            listar_todos()
        elif escolha == '2':
            nome = str(input('Escreva o nome do campeão: '))
            pesquisar_campeao(nome)
        elif escolha == '3':
            nome = str(input('Digite o nome do campeão: '))
            if not validar_campeao(nome) is None:
                nova_build = armazenar_itens()
                build(nome, nova_build)
            else:
                pass
        elif escolha == '4':
            nome = str(input('Escreva o nome do campeão: '))
            id_b = int(input('Escreva o id da build: '))
            visualizar_build(nome, id_b)
        elif escolha == '0':
            print("Até mais! ")
            break 
        else:
            print("Escolha errada tente novamente.")