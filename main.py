def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para validar si la entrada es un entero positivo
def validar_entero_positivo(valor):
    try:
        valor_entero = int(valor)
        if valor_entero <= 0:
            raise ValueError("El número debe ser positivo y diferente de cero.")
        return valor_entero
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido.")

# Solicitar al usuario que ingrese los números y validarlos
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        num1 = validar_entero_positivo(num1)
        break
    except ValueError as error:
        print(error)

while True:
    try:
        num2 = input("Ingrese el segundo número: ")
        num2 = validar_entero_positivo(num2)
        break
    except ValueError as error:
        print(error)

# Calcular el MCD utilizando la función definida anteriormente
mcd = calcular_mcd(num1, num2)

# Mostrar el resultado
print("El Máximo Común Divisor de", num1, "y", num2, "es:", mcd)


