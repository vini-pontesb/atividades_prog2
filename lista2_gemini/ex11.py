class ValorInvalidoError(Exception):
    pass

def processar_pagamento(valor):
    if valor <= 0:
        raise ValorInvalidoError(f"O valor {valor} não é permitido. Ele deve ser positivo")
    
    print(f"Pagamento de R${valor} processado!")

try:
    valor = float(input("Insira um valor que será processado: "))
    processar_pagamento(valor)
except ValorInvalidoError as e:
    print(f"ERRO: {e}.")