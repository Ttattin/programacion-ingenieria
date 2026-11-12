# Definimos una función con dos parámetros: a y b.
def sumar(a, b):
    print("Estamos dentro de la función sumar.")
    resultado = a + b
    print("La suma que devolveremos es:", resultado)
    return resultado


numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

# Llamamos a la función y guardamos el valor que devuelve.
suma = sumar(numero1, numero2)
print("La suma es:", suma)

# Podemos reutilizar la misma función con otros números.
otra_suma = sumar(10, 5)
print("La suma de 10 y 5 es:", otra_suma)
