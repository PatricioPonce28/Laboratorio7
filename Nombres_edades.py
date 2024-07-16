nombres = []
edades = []
estudiantes = 10 

for i in range (estudiantes) :
    nombre = (input(f"Ingrese su nombre del estudiante {i+1}: "))
    nombres.append(nombre)

for j in range(estudiantes) :
    edad = (input(f"Ingrese la edad del estudiante: {j+1}: "))
    edades.append(edad)

edad_mayor = max(edades)
indice_edad_mayor = edades.index(edad_mayor)
nombre_edad_mayor = nombres[indice_edad_mayor]

print(nombres)
print(edades)
print(f"El estudiante con la mayor edad es {nombre_edad_mayor} con {edad_mayor} años.")