import pytest
import calcolatrice

def test_somma():
    assert calcolatrice.somma(2, 2) == 4, "la funzione somma(2, 2) non ha prodotto 4!"
    assert calcolatrice.somma(3, 3) != 7
    assert calcolatrice.somma(0, -1) < 0

def test_divisione():
    assert calcolatrice.divisione(6, 3) == 2
    assert calcolatrice.divisione(10, 5) == 2
    with pytest.raises(ValueError):
        calcolatrice.divisione(1, 0)

# Aggiungi le funzioni per testare moltiplicazione e sottrazione
def test_moltiplicazione():
    assert calcolatrice.moltiplicazione(1, 5) == 5
    assert calcolatrice.moltiplicazione(1, 0) == 0
    assert calcolatrice.moltiplicazione(12, 10) > 100

def test_sottrazione():
    assert calcolatrice.sottrazione(5, 5) == 0
    assert calcolatrice.sottrazione(-1, 0) == -1
    assert calcolatrice.sottrazione(0, 1) == -1

# Aggiungi una funzione per testare magicNumbers
# bonus: prevedi di usare l'operatore in nell'assert
def test_magicNumbers():
    assert 15 in calcolatrice.magicNumbers(3, 50)
    assert 20 not in calcolatrice.magicNumbers(3, 50)
    assert 55 in calcolatrice.magicNumbers(3, 55)
