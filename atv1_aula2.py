#a
def matriz_a(n):
    for linha in range(1, n+1):
        for coluna in range(1, n+1):
            if coluna == linha:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
i = int(input("Insira um índice para a matriz: "))
matriz_a(i)

#b
def matriz_b(n):
    x = n
    for linha in range(1, n+1):
        for coluna in range(1, n+1):
            if coluna == linha or coluna == x:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
        x -= 1
i = int(input("Insira um índice para a matriz: "))
matriz_b(i) 

#c
def matriz_c(n):
    x = n
    for l in range (1, n+1):
        for c in range(1, n+1):
            if c==l or c==x or c==((n/2)+0.5):
                print(1, end=" ")
            else:
                print(0, end=" ")
        x -= 1
        print()
i = int(input("Insira um número intero, positivo e ímpar: "))
while i % 2 == 0:
    i = int(input("O número que você digitpu não é ímpar, insira novamente: "))
matriz_c(i)

#d
def matriz_d(n):
    x = n
    for l in range (1, n+1):
        for c in range(1, n+1):
            if c == l or c == x or c == ((n/2)+0.5) or l == ((n/2)+0.5):
                print(1, end=" ")
            else:
                print(0, end=" ")
        x -= 1
        print()
i = int(input("Insira um número intero, positivo e ímpar: "))
while i % 2 == 0:
    i = int(input("O número que você digitpu não é ímpar, insira novamente: "))
matriz_d(i)

#e
def matriz_d(n):
    x = ((n/2)+0.5)
    x2 = x
    x3 = x
    for l in range (1, n+1):
        for c in range(1, n+1):
            if c == x:
                print(1, end=" ")
            elif c >= x2 and c <= x3:
                print(1, end=" ")
            else:
                print(0, end=" ")
        x2 -= 1
        x3 += 1
        print()
i = int(input("Insira um número intero, positivo e ímpar: "))
while i % 2 == 0:
    i = int(input("O número que você digitpu não é ímpar, insira novamente: "))
matriz_d(i)

#f
def matriz_d(n):
    x = ((n/2)+0.5)
    x2 = 1 
    x3 = n
    for l in range (1, n+1):
        for c in range(1, n+1):
            if c == x:
                print(1, end=" ")
            elif c >= x2 and c <= x3:
                print(1, end=" ")
            else:
                print(0, end=" ")
        x2 += 1
        x3 -= 1
        print()
i = int(input("Insira um número intero, positivo e ímpar: "))
while i % 2 == 0:
    i = int(input("O número que você digitpu não é ímpar, insira novamente: "))
matriz_d(i)

altura = int(input('Digite a altura do Triângulo: '))

for i in range(altura):

    espacos = altura - i - 1
    numeros = 2 * i + 1
    print(" "* espacos + "1"*numeros)