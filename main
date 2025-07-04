# main.py

from calculator import calculator

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

def ask_if_continue(prompt="Vil du regne videre? (y/n): "):
    while True:
        cont = input(prompt).strip().lower()
        if cont in ['y', 'n']:
            return cont
        else:
            print("Skriv venligst 'y' eller 'n'.")


def ask_use_previous(result):
    while True:
        choice = input(f"Vil du bruge resultatet ({result}) som første tal? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Skriv venligst 'y' eller 'n'.")

def main():
    print("Velkommen til lommeregner programmet!")
    previous_result = None

    while True:
        try:
            if previous_result is not None and ask_use_previous(previous_result):
                a = previous_result
            else:
                a = get_number("Indtast første tal: ")

            operator = get_operator("Indtast operator (+, -, *, /): ")
            b = get_number("Indtast andet tal: ")

            result = calculator(a, operator, b)
            print("Resultat:", result)

            previous_result = result  # gem resultat til næste omgang
        except (TypeError, ValueError, ZeroDivisionError) as e:
            print(f"Fejl: {e}")
            continue

        cont = ask_if_continue()
        if cont == 'n':
            print("Tak for nu. Kom tilbage senere!")
            break

if __name__ == '__main__':
    main()