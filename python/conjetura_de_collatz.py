numero = int(input("Introduce un número entero positivo: "))

while numero <= 0:
    numero = int(input("Debe ser positivo. Introduce otro número: "))

contador = 0

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1

    print(numero)
    contador += 1

print("Número de valores generados:", contador)
