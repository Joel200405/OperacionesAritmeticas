def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular el MCD utilizando la función definida anteriormente
mcd = calcular_mcd(num1, num2)

# Mostrar el resultado
print("El Máximo Común Divisor de", num1, "y", num2, "es:", mcd)



