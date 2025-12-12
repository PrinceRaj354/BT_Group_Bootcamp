import pytest
from challenges.challenge_16_input_validation.validation import (
    validate_name, validate_empid, validate_basic_salary,
    validate_special_allowance, validate_bonus_percentage,
    validate_all
)

# ------------- NAME TESTS -----------------
def test_valid_name():
    assert validate_name("John Doe")

def test_invalid_name_empty():
    with pytest.raises(ValueError):
        validate_name("")

def test_invalid_name_characters():
    with pytest.raises(ValueError):
        validate_name("John123")

# ------------- EMPID TESTS -----------------
def test_valid_empid():
    assert validate_empid("EMP123")

def test_invalid_empid_short():
    with pytest.raises(ValueError):
        validate_empid("A1")

# ------------- BASIC SALARY -----------------
def test_basic_salary_valid():
    assert validate_basic_salary(50000)

def test_basic_salary_negative():
    with pytest.raises(ValueError):
        validate_basic_salary(-10)

# ------------- SPECIAL ALLOWANCE ------------
def test_special_allowance_negative():
    with pytest.raises(ValueError):
        validate_special_allowance(-5)

# ------------- BONUS PERCENTAGE -------------
def test_bonus_valid():
    assert validate_bonus_percentage(20)

def test_bonus_invalid():
    with pytest.raises(ValueError):
        validate_bonus_percentage(150)

# ------------- FULL VALIDATION --------------
def test_validate_all_valid():
    assert validate_all("Alice", "EMP999", 50000, 10000, 10)

def test_validate_all_invalid():
    with pytest.raises(ValueError):
        validate_all("A1", "EMP1", -100, 10000, 10)
