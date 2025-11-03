import requests
import json

base_url = 'http://127.0.0.1:8000'

def menu():
    endpoint = '/champion/all'
    url = base_url + endpoint
    
    try:
        res = requests.get(url)
    except:
        pass
    res.raise_for_status()
    dicionario = res.json()

    for champ, info in dicionario.items():
        print(f'{champ} - {info['title']}')

def campeao(nome):
    endpoint = f'/champion/{nome}'
    url = base_url + endpoint
    res = requests.get(url)
    res.raise_for_status()
    champ = res.json()
    print(f'{champ['id']} {champ['blurb']}')

def build(build_data: dict,nome, it1,it2,it3,it4,it5,it6):
    endpoint = f'/champion/{nome}/build'
    url = base_url + endpoint
    
menu()
campeao("Ahri")