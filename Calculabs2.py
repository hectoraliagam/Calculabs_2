# CALCULABS
# by Hector Aliaga

def print_title(title):
    for text in title:
        print(text)
    return

def print_menu(title,options):
    for text in title:
        print(text)
    for option in options:
        print(option)
    return

def print_menu_choise(title,options):
    for text in title:
        print(text)
    for option in options:
        print(option)
    choise = input("Inserta: ")
    if choise.isdigit():
        return int(choise)
    return choise

def menu_title():
    title = [
        "----------------------------------",
        "|     BIENVENIDO A CALCULABS     |"
    ]
    return print_title(title)

def version_title():
    title = [
        "----------------------------------",
        "|         Versión: 2.3.10         |"
    ]
    return print_title(title)

def exit_title():
    title = [
        "----------------------------------",
        "|      Gracias por utilizar      |",
        "|           CALCULABS            |",
        "|       Vuelva pronto! :D        |",
        "----------------------------------"
    ]
    return print_title(title)

def menu_opt():
    title = [
        "|--------------------------------|",
        "|    MENÚ PRINCIPAL:             |"
    ]
    options = [
        "|    Salir/Menú ---------- 0     |",
        "|    Versión ------------- 1     |",
        "|    Menú Math ----------- 2     |",
        "----------------------------------"
    ]
    return print_menu_choise(title,options)

# despues colocar funcion para version del programa

def math_menu_opt():
    title = [
        "----------------------------------",
        "|    MENÚ MATH:                  |"
    ]
    options = [
        "|    Volver/Menú Actual -- 0     |",
        "|    Operaciones --------- 1     |",
        "|    Promedios  ---------- 2     |",
        "----------------------------------"
    ]
    return print_menu_choise(title,options)

def average_menu_opt():
    title = [
        "----------------------------------",
        "|    MENÚ PROMEDIOS:             |"
    ]
    options = [
        "|    Volver/Menú Actual -- 0     |",
        "|    Aritmético ---------- 1     |",
        "|    Geométrico ---------- 2     |",
        "|    Armónico ------------ 3     |",
        "----------------------------------"
    ]
    return print_menu_choise(title,options)

def exit_menu_opt():
    while True:
        title = [
            "----------------------------------",
            "|       ¿Desea continuar?        |"
        ]
        options = [
            "|--------------------------------|",
            "|    Salir --------------- s     |",
            "|    Menú Principal ------ p     |",
            "----------------------------------"
        ]
        print_menu(title,options)
        exit_opt = input("Inserta: ")
        if exit_opt == "s":
            exit_title()
            return -1
        elif exit_opt == "p":
            return 0

def exit_math_menu_opt():
    while True:
        title = [
            "----------------------------------",
            "|       ¿Desea continuar?        |"
        ]
        options = [
            "|--------------------------------|",
            "|    Volver -------------- v     |",
            "|    Menú Math ----------- m     |",
            "----------------------------------"
        ]
        print_menu(title,options)
        exit_math_opt = input("Inserta: ")
        if exit_math_opt == "v":
            return -1
        elif exit_math_opt == "m":
            return 0

def exit_average_menu_opt():
    while True:
        title = [
            "----------------------------------",
            "|       ¿Desea continuar?        |"
        ]
        options = [
            "|--------------------------------|",
            "|    Volver -------------- v     |",
            "|    Menú Promedios ------ m     |",
            "----------------------------------"
        ]
        print_menu(title,options)
        exit_math_opt = input("Inserta: ")
        if exit_math_opt == "v":
            return -1
        elif exit_math_opt == "m":
            return 0

def get_number(prompt="Ingresa un número: "):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            continue

def perform_operation():
    title = [
        "----------------------------------",
        "|          OPERACIONES           |"
    ]
    options = [
        "|--------------------------------|",
        "|    Suma -------------- '+'     |",
        "|    Resta ------------- '-'     |",
        "|    Multiplicación ---- '*'     |",
        "|    División ---------- '/'     |",
        "|    Potenciación ----- '**'     |",
        "|    Radicación ------- '*/'     |",
        "|    Terminar ---------- '='     |",
        "----------------------------------"
    ]
    print_menu(title,options)
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
        return f"|    == {int(result)}"
    return f"|    == {result}"

def arithmetic_average():
    title = [
        "----------------------------------",
        "|      Promedio Aritmético       |",
    ]
    options = [
        "|--------------------------------|",
        "|    Terminar ---------- '='     |",
        "----------------------------------"
    ]
    print_menu(title,options)
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
    return f"|    == {add/num_of_nums}"

def geometric_average():
    title = [
        "----------------------------------",
        "|      Promedio Geométrico       |",
    ]
    options = [
        "|--------------------------------|",
        "|    Terminar ---------- '='     |",
        "----------------------------------"
    ]
    print_menu(title,options)
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
    return f"|    == {mul**(1/num_of_nums)}"

def harmonic_average():
    title = [
        "----------------------------------",
        "|       Promedio Armónico        |",
    ]
    options = [
        "|--------------------------------|",
        "|    Terminar ---------- '='     |",
        "----------------------------------"
    ]
    print_menu(title,options)
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
    return f"|    == {num_of_nums/add}"

# Main program

while True:
    menu_title()
    opt = menu_opt()
    if opt == 0:
        if exit_menu_opt() == -1:
            break
    elif opt == 1:
        version_title()
        if exit_menu_opt() == -1:
            break
    elif opt == 2:
        while True:
            opt_math = math_menu_opt()
            if opt_math == 0:
                if exit_math_menu_opt() == -1:
                    break
            elif opt_math == -1:
                break
            elif opt_math == 1:
                print(perform_operation())
                if exit_math_menu_opt() == -1:
                    break
            elif opt_math == 2:
                while True:
                    opt_average = average_menu_opt()
                    if opt_average == 0:
                        if exit_average_menu_opt() == -1:
                            break
                    elif opt_average == -1:
                        break
                    elif opt_average == 1:
                        print(arithmetic_average())
                        if exit_average_menu_opt() == -1:
                            break
                    elif opt_average == 2:
                        print(geometric_average())
                        if exit_average_menu_opt() == -1:
                            break
                    elif opt_average == 3:
                        print(harmonic_average())
                        if exit_average_menu_opt() == -1:
                            break
