def must_pay_tax(name, salary):

    if salary > 300000:
        return f"{name} must pay tax"
    else:
        return f"{name} does not need to pay tax"


if __name__ == "__main__":
    name = input("Enter name: ").strip()
    salary = float(input("Enter salary: ").strip())

    print(must_pay_tax(name, salary))
