from pytest import raises

from piknik import Contrib, totalizar, contabilizar, Ajuste


def test_construir_contrib():
    res = Contrib.construir('Ana', '10')
    assert res == Contrib('Ana', 10.0)


def test_construir_contrib_valor_não_numérico():
    with raises(ValueError):
        _ = Contrib.construir('Ana', 'dez')


def test_totalizar():
    contribs = [Contrib('Ana', 10.0), Contrib('Bia', 20.0)]
    assert totalizar(contribs) == 30.0


def test_contabilizar():
    contribs = [Contrib('Ana', 10.0), Contrib('Bia', 20.0)]
    res = contabilizar(contribs)
    assert res == [
        Ajuste(Contrib('Ana', 10.0), 'pagar', 5.0),
        Ajuste(Contrib('Bia', 20.0), 'receber', 5.0),
    ]

