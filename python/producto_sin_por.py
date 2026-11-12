numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

valor1 = abs(numero1)
valor2 = abs(numero2)
producto = 0

# Sumamos el primer valor tantas veces como indica el segundo.
for contador in range(valor2):
    print("el contador vale:", contador)
    producto = producto + valor1
    print("el producto vale:", producto)

# El resultado es negativo si los números tienen signos distintos.
if numero1 < 0 and numero2 > 0:
    producto = -producto
elif numero1 > 0 and numero2 < 0:
    producto = -producto

print("El producto es:", producto)
