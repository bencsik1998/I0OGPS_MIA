from calculator import Calculator

def test_integration_add_subtract():
    calc = Calculator()
    result = calc.add(5, 3)
    result = calc.subtract(result, 2)
    assert result == 6