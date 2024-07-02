def calcoloFattoriale(x):
    # non ricorsivo --> x! = x*(x-1)*(x-2)*(x-N)...*1
    fattoriale = x

    # Caso base
    if x == 0 or x == 1:
        return 1

    for i in range(1, x):
        fattoriale *= i

    # Analogo a
    # for i in range(x-1, 1, -1):
    #     fattoriale *= i

    return fattoriale

def somma (x,y):
    return x + y


def sottrazione (x,y):
    return x - y

def divsione (num,den):
    if den == 0:
        return 'Non è possibile dividere per 0'
    else:
        return num/den

def moltiplicazione (x,y):
    return x * y

def dispariInteri(numeri):
    return [i for i in numeri if i % 2 != 0 and  i % 5 == 0]
