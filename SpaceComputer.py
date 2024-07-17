import random
nombres = []
huella_facial = []
codigo = []

def main():
    print("Bienvenido a Space Computer")
    print("Control biométrico")
    while True:
        opcion = menuOptions()
        if opcion == 1:
            registrarUsuarios()
        elif opcion == 2:
            login()
        elif opcion == 3:
            print("Saliendo del sistema...")
            break

def menuOptions():
    print("1) Registro de Usuarios")
    print("2) Login")
    print("3) Salir del sistema")
    opcion = int(input("Ingresa la opción que deseas realizar: "))
    while opcion not in [1, 2, 3]:
        print("Opción incorrecta, pruébelo de nuevo.")
        opcion = int(input("Ingresa la opción que deseas realizar: "))
    return opcion

def registrarUsuarios():
    num_registrados = int(input("Ingrese el número de personas que va a ingresar: "))
    if num_registrados > 20 or num_registrados <= 0:
        print("El número de registrados debe estar entre 1 y 20")
    else:
        for i in range(num_registrados):
            while True:
                nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
                if nombre.isalpha():
                    break
                else:
                    print("El nombre solo puede contener letras. Inténtelo de nuevo.")
            nombres.append(nombre)
            huella_facial_persona = input(f"Ingrese la huella facial de la persona {i + 1}: ")
            huella_facial.append(huella_facial_persona)
            codigo.append(random.randrange(1000, 9999))
        print("Registro completado.")
        
def login():
    if len(nombres) == 0 and len(huella_facial) == 0:
        print("No existen registros")
        return 
    
    nombre_verificacion = input("Ingrese su nombre: ")
    huella_verificacion = input("Ingrese su huella: ")

    if nombre_verificacion in nombres:
        index = nombres.index(nombre_verificacion)
        if huella_facial[index] == huella_verificacion:
            print(f"Bienvenido {nombre_verificacion}, acceso concedido.")
            print(f"Tus datos son los siguientes:")
            print(f"Nombre: {nombres[index]}")
            print(f"Huella Facial: {huella_facial[index]}")
            print(f"Código: {codigo[index]}")
        else:
            print("Huella facial incorrecta")
    else:
        print("Nombre no encontrado")

main()
