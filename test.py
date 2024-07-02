import pytest
import matematica

def test_somma():
    assert matematica.somma(2, 2) == 4, "la funzione somma(2, 2) non ha prodotto 4!"
    assert matematica.somma(3, 3) != 7
    assert matematica.somma(0, -1) < 0

def test_divisione():
    assert matematica.divisione(6, 3) == 2
    assert matematica.divisione(10, 5) == 2
    with pytest.raises(ValueError):
        matematica.divisione(1, 0)