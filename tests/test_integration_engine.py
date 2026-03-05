from quick_calc.engine import CalculatorEngine

def test_full_user_interaction_addition():
    eng = CalculatorEngine()
    eng.press("5")
    eng.press("+")
    eng.press("3")
    result = eng.press("=")
    assert result == "8"

def test_clear_resets_after_calculation():
    eng = CalculatorEngine()
    eng.press("9")
    eng.press("*")
    eng.press("9")
    eng.press("=")
    assert eng.display == "81"
    assert eng.press("C") == "0"
    assert eng.display == "0"