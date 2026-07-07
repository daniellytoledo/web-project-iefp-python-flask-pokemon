from app.models.rep_pokemon_cards import select_cards, select_card_id, select_types, insert_into_cards
from pprint import pprint

def lista_cards():
    return select_cards()

def detalhes_card(card_id):
    return select_card_id(card_id)

def lista_tipos():
    return select_types()

def adicionar_pokemon(nome, tipo, desc, img):
    return insert_into_cards(nome, tipo, desc, img)