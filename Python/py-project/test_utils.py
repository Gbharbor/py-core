from utils import dar_oi, somar 

def test_dar_oi():
    assert dar_oi("Gui") == "ola, eu sou Gui"
def test_somar_normal():
    assert somar(10,5) == 15
def test_somar_igual():
    assert somar(1, 1) == 2
def test_somar_negativo():
    assert somar(-5, 7) == 2
    