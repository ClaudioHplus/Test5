import pytest
import math
from classiGeometriche import Poligono, Triangolo, TriangoloRettangolo, TriangoloIsoscele, TriangoloEquilatero, sommaPoligoni

def test_Poligono():
    lati = [3, 4, 5]
    angoli = [90, 45, 45]
    p = Poligono(lati, angoli)
    
    assert isinstance(p, Poligono)
    assert p.lati == lati
    assert p.angoli == angoli
    assert p.calcolaPerimetro() == 12
    assert p.sommaAngoli() == 180

def test_Triangolo():
    t = Triangolo(3, 4, 5, 90, 45, 45)
    
    assert isinstance(t, Triangolo)
    assert t.calcolaPerimetro() == 12
    assert t.sommaAngoli() == 180
    assert t.calcolaArea() != 6.0
   

def test_TriangoloRettangolo():
    tr = TriangoloRettangolo(3, 4, 5, 90, 45, 45)
    
    assert isinstance(tr, TriangoloRettangolo)
    assert tr.calcolaPerimetro() == 12
    assert tr.sommaAngoli() == 180
    assert tr.calcolaArea() == 6.0
    assert tr.altezza == 4

def test_TriangoloIsoscele():
    ti = TriangoloIsoscele(3, 4, 45, 90)
    
    assert isinstance(ti, TriangoloIsoscele)
    assert ti.calcolaPerimetro() == 11
    assert ti.sommaAngoli() == 180
    

def test_TriangoloEquilatero():
    te = TriangoloEquilatero(3)
    
    assert isinstance(te, TriangoloEquilatero)
    assert te.calcolaPerimetro() == 9
    assert te.sommaAngoli() == 180

def test_sommaPoligoni():
    p1 = Poligono([3, 4, 5], [90, 45, 45])
    p2 = Poligono([6, 7, 8], [80, 50, 50])
    
    assert sommaPoligoni(p1, p2) == 33

def test_Triangolo_equality():
    t1 = Triangolo(3, 4, 5, 90, 45, 45)
    t2 = Triangolo(3, 4, 5, 90, 45, 45)
    t3 = Triangolo(3, 4, 6, 90, 45, 45)
    
    assert t1 == t2
    assert t1 != t3

def test_Triangolo_addition():
    t1 = Triangolo(3, 4, 5, 90, 45, 45)
    t2 = Triangolo(3, 4, 5, 90, 45, 45)
    
    assert t1 + t2 != 12.0


if __name__ == '__main__':
    pytest.main()
