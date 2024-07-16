def main():
    print("Bienvenido al Náufrago Satisfecho")
    num_hamburguesas = int(input("Ingrese el número de hamburguesas que va a comprar: "))
    suma_hamburguesas = 0

    for i in range(num_hamburguesas):
        tipo_hamburguesa = menu_options(i + 1)
        if tipo_hamburguesa == "S":
            suma_hamburguesas += 20
        elif tipo_hamburguesa == "D":
            suma_hamburguesas += 25
        elif tipo_hamburguesa == "T":
            suma_hamburguesas += 28

    pago_tarjeta = input("¿Va a pagar con tarjeta de crédito? (si/no): ").strip().lower()
    if pago_tarjeta == "si":
        suma_hamburguesas *= 1.05

    print(f"El total a pagar es: ${suma_hamburguesas:.2f}")

def menu_options(hamburguesa_num):
    print(f"\nElige el tipo de hamburguesa {hamburguesa_num}:")
    print("S) Sencilla -------------------- $20")
    print("D) Doble ----------------------- $25")
    print("T) Triple ---------------------- $28")
    opcion = input("Ingrese la opción (S/D/T): ").strip().upper()
    while opcion !="S" or opcion!="D" or opcion != "T" :
        print("Opción inválida, pruebe de nuevo.")
        opcion = input("Ingrese la opción (S/D/T): ").strip().upper()
    return opcion

main()
