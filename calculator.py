# calculator.py

def calculator(a, operator, b):
    if not isinstance(a, (int, float)):
        raise TypeError("Første parameter skal være et tal")
    if not isinstance(b, (int, float)):
        raise TypeError("Andet parameter skal være et tal")
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Operator skal være en af '+', '-', '*', '/'")

    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError("Division med nul er ikke tilladt")
            return a / b
