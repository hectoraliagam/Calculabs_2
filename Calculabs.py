def menu_opc():
    print("------------------")
    print("Bienvenidos a Calculabs")
    print("He aqui el menu de opciones:")
    print("Salir/Menu -------- 0")
    print("Version ----------- 1")
    print("Menu Oper --------- 2")
    opc = input("Inserta: ")
    if opc.isdigit():
        opc = int(opc)
        return opc
    else:
        return opc

def menu_opc_esp():
    print("------------------")
    print("Volver/Menu_op ---- 0")
    print("Operaciones ------- 1")
    print("Promedio Arit ----- 2")
    print("Promedio Geom ----- 3")
    print("Promedio Armo ----- 4")
    opc_esp = input("Inserta: ")
    if opc_esp.isdigit():
        opc_esp = int(opc_esp)
        return opc_esp
    else:
        return opc_esp

def opc_exit_menu():
    while True:
        print("------------------")
        opc_exit = input("¿Desea continuar? (salir 'e', menu principal 'p'): ")
        if opc_exit == 'e':
            print("------------------")
            print("Gracias por utilizar el programa, vuelva pronto! :D")
            print("------------------")
            return -1
        elif opc_exit == 'p':
            opc = 0
            return opc
        else:
            continue

def opc_exit_menu_esp():
    while True:
        print("------------------")
        opc_exit_esp = input("¿Desea continuar? (volver 'v', menu math 's'): ")
        if opc_exit_esp == 'v':
            opc_esp = -1
            return opc_esp
        elif opc_exit_esp == 's':
            opc_esp = 0
            return opc_esp 
        else:
            continue

def operacion():
    print("Operaciones disponibles: suma '+', resta '-', multiplicacion '*', division '/',")
    print("                         potenciacion '**', radicacion '*/', terminar '='")
    
    while True:
        resultado = input("Ingresa un numero: ")
        if resultado.replace(".","",1).isdigit():
            resultado = float(resultado)
            break
        
    while True:
        operacion = input("Ingresa una operacion: ")
        if operacion in ['+', '-', '*', '/', '**', '*/', '=']:
            if operacion == '=':
                break
            
            while True:
                num = input("Ingresa un numero: ")
                if num.replace(".","",1).isdigit():
                    num = float(num)
                    if operacion == '/' and num == 0:
                        print("Division por cero")
                        continue
                    break
            
            if operacion == '+':
                resultado += num
            elif operacion == '-':
                resultado -= num
            elif operacion == '*':
                resultado *= num
            elif operacion == '/':
                resultado /= num
            elif operacion == '**':
                resultado **= num
            elif operacion == '*/':
                resultado **= 1/num
            
    print("------------------")
    return resultado

def promedio_aritmetico():
    print("Ingresa un numero o '=' para terminar")
    
    while True:
        num = input("Ingresa: ")
        if num.replace('.','',1).isdigit():
            num = float(num)
            break
    
    suma = num
    cant_num = 1
    
    while True:
        num = input("Ingresa: ")
        if num == "=":
            print("------------------")
            break
        elif num.replace('.','',1).isdigit():
            num = float(num)
            suma += num
            cant_num += 1
            
    prom_total = suma/cant_num
    return prom_total

def promedio_geometrico():
    print("Ingresa un numero o '=' para terminar")
    
    while True:
        num = input("Ingresa: ")
        if num.replace('.','',1).isdigit():
            num = float(num)
            break
    
    multi = num
    cant_num = 1
    
    while True:
        num = input("Ingresa: ")
        if num == '=':
            print("------------------")
            break
        elif num.replace('.','',1).isdigit():
            num = float(num)
            multi *= num
            cant_num += 1
    
    prom_total = multi**(1/cant_num)
    return prom_total

def promedio_armonico():
    print("Ingresa un numero o '=' para terminar")
    
    while True:
        num = input("Ingresa: ")
        if num.replace('.','',1).isdigit():
            num = float(num)
            break
    
    suma = 1/num
    cant_num = 1
    
    while True:
        num = input("Ingresa: ")
        if num == '=':
            print("------------------")
            break
        elif num.replace('.','',1).isdigit():
            num = float(num)
            suma += 1/num
            cant_num += 1
    
    prom_total = cant_num/suma
    return prom_total

while True:
    
    opc = menu_opc()
    if opc == 0:
        opc = opc_exit_menu()
        if opc_exit_menu() == -1:
            break
        else:
            continue
    
    elif opc == 1:
        print("------------------")
        print("Version: 1.6.6")
        opc = opc_exit_menu()
        
    elif opc == 2:
        
        while True:
            
            opc_esp = menu_opc_esp()
            if opc_esp == 0:
                opc_esp = opc_exit_menu_esp()
            elif opc_esp == -1:
                opc = menu_opc()
                break
                
            elif opc_esp == 1:
                print(f"La respuesta es {operacion()}")
                opc_esp = opc_exit_menu_esp()
                
            elif opc_esp == 2:
                print(f"La respuesta es {promedio_aritmetico()}")
                opc_esp = opc_exit_menu_esp()
            
            elif opc_esp == 3:
                print(f"La respuesta es {promedio_geometrico()}")
                opc_esp = opc_exit_menu_esp()
                
            elif opc_esp == 4:
                print(f"La respuesta es {promedio_armonico()}")
                opc_esp = opc_exit_menu_esp()
                
            else:
                opc_esp = menu_opc_esp()

#Hay un problema que ocurre cada vez que luego de haber colocado en el segundo menu la tecla 0 y despues colocado la v para volver, pasa que si el usuario ingresa cualquier tecla, el programa me envia al menu secundario :/
