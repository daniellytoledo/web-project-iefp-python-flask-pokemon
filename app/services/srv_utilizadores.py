from app.models.rep_utilizadores import select_nome_utilizador, insert_utilizador, select_todos_utilizadores
from pprint import pprint
from werkzeug.security import generate_password_hash, check_password_hash

from flask import url_for, current_app
from itsdangerous import URLSafeTimedSerializer
import logging

def listar_utilizadores():
    listar_utilizadores = select_todos_utilizadores()
    return listar_utilizadores

def gerar_hash_password_igual_nome_u():
    listar_utilizadores = select_todos_utilizadores()
    for utilizador in listar_utilizadores:
        print(generate_password_hash(utilizador['nome_u']))

if __name__== "__main__":
    pprint(gerar_hash_password_igual_nome_u())