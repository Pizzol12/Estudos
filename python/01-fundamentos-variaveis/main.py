"""Exemplo introdutório sobre variáveis e tipos de dados em Python."""

idade = 18
altura = 1.82
peso = 72.0
nome = "Davi"
cidade = "Guarapari"
estudante = True
trabalha = False

variaveis = {
    "idade": idade,
    "altura": altura,
    "peso": peso,
    "nome": nome,
    "cidade": cidade,
    "estudante": estudante,
    "trabalha": trabalha,
}

for identificador, valor in variaveis.items():
    print(f"{identificador}: {valor!r} — tipo {type(valor).__name__}")

