import pytest
from calculator import Calculator, Operation  

@pytest.fixture
def calc():
    return Calculator("Test Calculator")

def test_add(calc):
    assert calc.calculate(2, 3, Operation.ADD) == 5

def test_sub(calc):
    assert calc.calculate(5, 3, Operation.SUB) == 2

def test_mul(calc):
    assert calc.calculate(4, 3, Operation.MUL) == 12

def test_div(calc):
    assert calc.calculate(10, 2, Operation.DIV) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.calculate(10, 0, Operation.DIV)

def test_invalid_operation(calc):
    with pytest.raises(ValueError):
        calc.calculate(10, 2, 5)

def test_get_operator_as_character(calc):
    assert calc.get_operator_as_character(Operation.ADD) == "+"
    assert calc.get_operator_as_character(Operation.SUB) == "-"
    assert calc.get_operator_as_character(Operation.MUL) == "*"
    assert calc.get_operator_as_character(Operation.DIV) == "/"

def test_get_operator_unknown(calc):
    class FakeOperation:
        pass
    assert calc.get_operator_as_character(FakeOperation()) == "?"

def test_print_history_output(calc, capsys):
    calc.calculate(2, 3, Operation.ADD)
    calc.calculate(5, 2, Operation.SUB)
    calc.print_history()
    captured = capsys.readouterr()
    assert f"{calc.title} History:" in captured.out
    assert "2 + 3 = 5" in captured.out
    assert "5 - 2 = 3" in captured.out
