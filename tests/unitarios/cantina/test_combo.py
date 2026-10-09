import pytest 
from app.cantina.combo import calcular_desconto_combo


@pytest.mark.parametrize(
    "quantidade, perfil, desconto_esperado",
    [
     (1,"estudante" , 0.0),
     (2,"estudante" , 0.15),
     (3,"estudante" , 0.15),
     (4,"professor" , 0.10),
     (5,"visitante" , 0.0),
     (0,"estudante" , 0.0),

    ]
)
def test_calcular_desconto_combo_cenarios(quantidade, perfil, desconto_esperado):
    resultado = calcular_desconto_combo(quantidade, perfil)
    assert resultado == desconto_esperado