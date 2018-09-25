# -*- coding: utf-8 -*-

import sys, os
from datetime import datetime
from time import sleep

import pandas as pd

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

MY_FILE = os.path.join(WORKING_DIR, 'my_file.txt')

def now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print('Inicio: %s' % now_str())
sleep(0.5)
print('Criando linhas...')
sleep(0.5)
meu_texto = [
    'Este é meu arquivo de texto.\n',
    'Ele contém algumas linhas, que serão escritas no meu arquivo.\n'
]
print('Criando arquivo de texto em: %s' % MY_FILE)
sleep(1)
try:
    with open(MY_FILE, 'w', encoding='utf-8') as file:
        file.writelines(meu_texto)
        file.close()
except Exception as e:
    print('Erro ao tentar criar o arquivo %s\nErro: %s' % (MY_FILE, str(e)))
    sys.exit()
sleep(2)
print('Arquivo criado com sucesso!')
sleep(0.5)
print('Fim: %s' % now_str())
