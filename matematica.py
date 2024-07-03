
def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError
    return num / den

# Aggiungi le funzioni moltiplicazione e sottrazione
def sottrazione(a: int | float, b: int | float) -> int | float:
    return a - b

def moltiplicazione(a: int | float, b: int | float) -> int | float:
    return a * b

# Aggiungi una funzione magicNumbers per restituire una lista di tutti e soli i numeri interi dispari e multipli di 5 tra start e stop
# bonus: fallo su una unica riga con la list comprehension
def magicNumbers(start: int, stop: int) -> list[int]:
    return [numero for numero in range(start, stop + 1) if not numero % 5 and numero % 2]

# def magicNumbers(numeri):
#     lista = []
#     for numero in range(start, stop):
#         lista.append(numero)

#     return [i for i in numeri if i % 2 != 0 and  i % 5 == 0]
