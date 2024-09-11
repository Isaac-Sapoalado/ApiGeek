

def calcular_preco(preco):

    if isinstance(preco,str):
        preco = 1
    if preco < 0:
        preco = abs(preco)
    if preco == 0:
        preco = 1
    return preco
