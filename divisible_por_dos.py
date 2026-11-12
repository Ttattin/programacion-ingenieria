numero = int(input("Introduce un número entero: "))

if numero == 0:
    print("El 0 se puede dividir entre 2 indefinidamente.")
else:
    veces = 0

    while numero % 2 == 0:
        numero = numero // 2
        veces = veces + 1

    print(f"Es {veces} veces divisible entre 2.")
