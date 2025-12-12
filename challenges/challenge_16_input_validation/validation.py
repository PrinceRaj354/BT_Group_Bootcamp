import re

# ----------------- NAME VALIDATION ------------------
def validate_name(name: str) -> bool:
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")
    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters.")
    if not re.fullmatch(r"[A-Za-z ]+", name):
        raise ValueError("Name must contain alphabets only.")
    return True


# ----------------- EMPLOYEE ID VALIDATION ------------
def validate_empid(empid: str) -> bool:
    if not re.fullmatch(r"[A-Za-z0-9]{5,10}", empid):
        raise ValueError("EmpID must be 5–10 alphanumeric characters.")
    return True


# ----------------- SALARY VALIDATION -----------------
def validate_basic_salary(value: float) -> bool:
    if value <= 0:
        raise ValueError("Basic salary must be a positive number.")
    if value > 10000000:
        raise ValueError("Basic salary cannot exceed ₹1,00,00,000.")
    return True


def validate_special_allowance(value: float) -> bool:
    if value < 0:
        raise ValueError("Special allowance cannot be negative.")
    if value > 10000000:
        raise ValueError("Special allowance cannot exceed ₹1,00,00,000.")
    return True


def validate_bonus_percentage(value: float) -> bool:
    if value < 0 or value > 100:
        raise ValueError("Bonus percentage must be between 0 and 100.")
    return True


# ----------------- DERIVED CALCULATION VALIDATION ----
def validate_gross_monthly(gross: float) -> bool:
    if gross <= 0:
        raise ValueError("Gross monthly salary must be greater than zero.")
    return True


def validate_annual_gross(annual: float) -> bool:
    if annual > 50000000:  # Arbitrary realistic limit
        raise ValueError("Annual gross salary exceeds realistic limits.")
    return True


# ----------------- INPUT WRAPPER ---------------------
def validate_all(name, empid, basic, allowance, bonus):
    """
    Validates all inputs together.
    Returns True if everything is valid.
    """
    validate_name(name)
    validate_empid(empid)
    validate_basic_salary(basic)
    validate_special_allowance(allowance)
    validate_bonus_percentage(bonus)

    gross_monthly = basic + allowance
    validate_gross_monthly(gross_monthly)

    annual_gross = gross_monthly * 12 + (gross_monthly * bonus / 100)
    validate_annual_gross(annual_gross)

    return True
