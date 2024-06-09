# CALCULABS
# by Hector Aliaga

def print_main(title,options):
    print("----------------------------------")
    print(title)
    for option in options:
        print(option)
    choise = input("Inserta: ")
    if choise.isdigit():
        return int(choise)
    return choise

def main_opt():
    options = [
        "|    Salir/Menú ---------- 0     |",
        "|    Versión ------------- 1     |",
        "|    Menú Math ----------- 2     |",
        "----------------------------------"
    ]
    return print_main("|    MENÚ PRINCIPAL:             |",options)

def main_opt_math():
    options = [
        "|    Volver/Menú Math ---- 0     |",
        "|    Operaciones --------- 1     |",
        "|    Promedio Arit ------- 2     |",
        "|    Promedio Geom ------- 3     |",
        "|    Promedio Armo ------- 4     |",
        "----------------------------------"
    ]
    return print_main("|    MENÚ MATH:                  |",options)

def print_exit_main(title_exit,options_exit):
    print("----------------------------------")
    print(title_exit)
    for option in options_exit:
        print(option)
    return

def opt_exit_main():
    while True:
        options = [
            "|    Salir --------------- s     |",
            "|    Menú Principal ------ p     |",
            "----------------------------------"
        ]
        print_exit_main("|       ¿Desea continuar?        |",options)
        opt_exit = input("Inserta: ")
        if opt_exit == "s":
            print("""---------------------------------------
|  Gracias por utilizar el programa,  |
|          vuelva pronto! :D          |
---------------------------------------""")
            return -1
        elif opt_exit == "p":
            return 0

def opt_exit_main_math():
    while True:
        options = [
            "|    Volver -------------- v     |",
            "|    Menú Math ----------- m     |",
            "----------------------------------"
        ]
        print_exit_main("|       ¿Desea continuar?        |",options)
        opt_exit_math = input("Inserta: ")
        if opt_exit_math == "v":
            return -1
        elif opt_exit_math == "m":
            return 0

def get_number(prompt="Ingresa un número: "):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            continue

def print_main_math(title_math,options_math):
    print("----------------------------------")
    print(title_math)
    for option in options_math:
        print(option)
    return

def operation():
    options = [
            "|    Suma -------------- '+'     |",
            "|    Resta ------------- '-'     |",
            "|    Multiplicación ---- '*'     |",
            "|    División ---------- '/'     |",
            "|    Potenciación ----- '**'     |",
            "|    Radicación ------- '*/'     |",
            "|    Terminar ---------- '='     |",
            "----------------------------------"
        ]
    print_exit_main("|    Operaciones disponibles:    |",options)
    result = get_number()
    while True:
        operation = input("Ingresa una operación: ")
        if operation == '=':
            break
        elif operation in ['+', '-', '*', '/', '**', '*/']:
            num = get_number()
            if operation == '/' and num == 0:
                print("|        División por cero       |")
                continue
            elif operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/':
                result /= num
            elif operation == '**':
                result **= num
            elif operation == '*/':
                result **= (1 / num)
            #result = eval(f"result {operation} num")
    print("----------------------------------")
    if result.is_integer():
        return int(result)
    return result

def arithmetic_average():
    print("----------------------------------")
    print("|      Promedio Aritmético:      |")
    print("|    Terminar ---------- '='     |")
    print("----------------------------------")
    add = get_number()
    num_of_nums = 1
    while True:
        num = input("Ingresa: ")
        if num == "=":
            print("----------------------------------")
            break
        try:
            add += float(num)
            num_of_nums += 1
        except ValueError:
            continue
    return add/num_of_nums

def geometric_average():
    print("----------------------------------")
    print("|      Promedio Geométrico:      |")
    print("|    Terminar ---------- '='     |")
    print("----------------------------------")
    mul = get_number()
    num_of_nums = 1
    while True:
        num = input("Ingresa: ")
        if num == "=":
            print("----------------------------------")
            break
        try:
            mul *= float(num)
            num_of_nums += 1
        except ValueError:
            continue
    return mul**(1/num_of_nums)

def harmonic_average():
    print("----------------------------------")
    print("|       Promedio Armónico:       |")
    print("|    Terminar ---------- '='     |")
    print("----------------------------------")
    add = 1/get_number()
    num_of_nums = 1
    while True:
        num = input("Ingresa: ")
        if num == "=":
            print("----------------------------------")
            break
        try:
            add += 1/float(num)
            num_of_nums += 1
        except ValueError:
            continue
    return num_of_nums/add

while True:
    print("----------------------------------")
    print("|     BIENVENIDO A CALCULABS     |")
    opt = main_opt()
    if opt == 0:
        if opt_exit_main() == -1:
            break
    elif opt == 1:
        print("----------------------------------")
        print("|         Versión: 2.2.5         |")
        if opt_exit_main() == -1:
            break
    elif opt == 2:
        while True:
            opt_math = main_opt_math()
            if opt_math == 0:
                if opt_exit_main_math() == -1:
                    break
            elif opt_math == -1:
                break
            elif opt_math == 1:
                
                #print(f"|    Salir --------------- s     |")
                print(f"|    == {operation()}")
                if opt_exit_main_math() == -1:
                    break
            elif opt_math == 2:
                
                print(f"|    == {arithmetic_average()}")
                if opt_exit_main_math() == -1:
                    break
            elif opt_math == 3:
                
                print(f"|   == {geometric_average()}")
                if opt_exit_main_math() == -1:
                    break
            elif opt_math == 4:
                
                print(f"|   == {harmonic_average()}")
                if opt_exit_main_math() == -1:
                    break
