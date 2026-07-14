from app.models.rep_autenticacao import validar_dados_de_login
from werkzeug.security import check_password_hash

def validar_login(utilizador, password):
    dados = validar_dados_de_login(utilizador)
    if "mensagem" in dados:
        return {
            "sucesso": False,
            "mensagem": dados["mensagem"]
        }
    if check_password_hash(dados["ppass_u"], password):
        return {
            "sucesso": True,
            "utilizador": {
                "id": dados["id_u"],
                "nome": dados["nome_u"],
                "nivel": dados["nivel_u"]
            }
        }
    
    return {
        "sucesso": False,
        "mensagem": "Password incorreto!"
    }