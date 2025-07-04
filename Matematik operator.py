def calculator(a, operator, b):
    if not isinstance(a, (int, float)):
        raise TypeError("Første parameter skal være et tal")
    if not isinstance(b, (int, float)):
        raise TypeError("Andet parameter skal være et tal")
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Operator skal være en af '+', '-', '*', '/'")

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Division med nul er ikke tilladt")
        return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ugyldigt tal, prøv igen.")


def get_operator(prompt):
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Operationen er ikke understøttet. Plus, minus, gange og division understøttes.")

def ask_if_continue(prompt = "Vil du regne videre? (y/n)"):
    while True:
        cont = input(prompt).strip().lower()
        if cont in ['y' , 'n']:
            return cont
        
        
    


def main():
    print("Velkommen til lommeregner programmet!")
    while True:
        try:
            a = get_number("Indtast første tal: ")
            operator = get_operator("Indtast operator (+, -, *, /): ")
            b = get_number("Indtast andet tal: ")

            result = calculator(a, operator, b)
        except (TypeError, ValueError, ZeroDivisionError) as e:
            print(f"Fejl: {e}")
            continue  # spring tilbage til starten af løkken og prøv igen

        print("Resultat:", result)

        cont = input("Vil du regne videre? (y/n): ").lower()
        if cont != 'y':
            print("Tak for nu. Kom tilbage senere!")
            break


if __name__ == '__main__':
    main()

