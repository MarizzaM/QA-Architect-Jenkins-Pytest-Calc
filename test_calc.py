import calc
import pytest


@pytest.mark.calc
@pytest.mark.parametrize("a,b,res", [(1, 1, 2), (0, 25, 25)])
def test_add_operation_positive_flow(a, b, res):
    assert calc.add(a, b) == res


@pytest.fixture
def x():
    return 'x'


def test_add_operation_negative_flow(x):
    with pytest.raises(TypeError):
        calc.dif(x, x)


@pytest.mark.calc
@pytest.mark.parametrize("a,b,res", [(1, 1, 0), (0, 25, -25)])
def test_dif_operation_positive_flow(a, b, res):
    assert calc.dif(a, b) == res


def test_dif_operation_negative_flow(x):
    with pytest.raises(TypeError):
        calc.dif(x, x)


@pytest.mark.calc
@pytest.mark.parametrize("a,b,res", [(1, 1, 1), (0, 25, 0)])
def test_mul_operation_positive_flow(a, b, res):
    assert calc.mul(a, b) == res


def test_mul_operation_negative_flow(x):
    with pytest.raises(TypeError):
        calc.mul(x, x)


@pytest.mark.calc
@pytest.mark.parametrize("a,b,res", [(1, 1, 1), (0, 25, 0)])
def test_div_operation_positive_flow(a, b, res):
    assert calc.div(a, b) == res


def test_div_operation_negative_flow(x):
    with pytest.raises(TypeError):
        calc.div(x, x)


@pytest.fixture
def zero():
    return 0


@pytest.mark.calc
def test_div_by_zero_negative_flow_div(zero):
    with pytest.raises(ZeroDivisionError):
        calc.div(4, zero)
