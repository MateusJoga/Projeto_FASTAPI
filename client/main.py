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
            print(f'{champ} - {info['title']}')
    except Exception as e:
        print(f'Erro: {e}')

def pesquisar_campeao(nome):
    endpoint = f'/champion/{nome}'
    url = base_url + endpoint
    try:
        res = requests.get(url)
        res.raise_for_status()
        champ = res.json()
        print(f'{champ['id']}: {champ['title']}')
    except Exception as e:
        print(f"Erro: {e}")

def build(nome, items):
    endpoint = f'/champion/{nome}/build'
    url = base_url + endpoint
    
    print(f"\n--- Enviando POST para: {url} com dados: {items} ---")
    
    res = None
    try:
        res = requests.post(url, json=items)
        res.raise_for_status()
        print("Resposta do Servidor: ", res.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ou receber resposta do servidor: {e}")
        if res is not None:
             print("Resposta de Erro: ", res.text)

def armazenar_itens():
    items = {}
    for i in range(6):
        items[f'item{i+1}'] = input(f'Digite o nome do {i+1}° item: ')
    return items

def menu():
    print('='*50)
    print('|X|X|X| CAMPEÕES DO LEAGUE OF LEGENDS |X|X|X|')
    print('1-Listar todos os campeões')
    print('2-Listar um campeão')
    print('3-Inserir build em um campeão')
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
            dicionario = armazenar_itens()
            print(dicionario)
            build(nome, dicionario)
        elif escolha == '0':
            print("Até mais! ")
            break 
        else:
            print("escolha errada tente novamente.")