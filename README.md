# Funciones de python


* Construir una función que reciba su nombre como parámetro y que lo muestre 5 veces en la pantalla.
```
def mostrar_nombre(nombre):
    for _ in range(5):
        print(nombre)


mostrar_nombre("Carlos")
```

* Construir una función que reciba una cadena digitada (como parámetro) por el usuario y que lo muestre n veces en la pantalla. El valor de n también es digitado por el usuario.
```
def repetir_cadena(cadena, n):
    for _ in range(n):
        print(cadena)

texto = input("Ingrese una cadena de texto: ")
veces = int(input("Ingrese el número de veces que desea repetirla: "))


repetir_cadena(texto, veces)

```

* Construir una función que reciba como parámetro una lista de datos numéricos y retorne la suma de dichos datos.

```
def sumar_lista(numeros):
    return sum(numeros)


lista_numeros = [1, 2, 3, 4, 5]
resultado = sumar_lista(lista_numeros)
print("La suma de los números es:", resultado)

```

* Construir una función que reciba como parámetro una lista de datos numéricos y que retorne el promedio de dichos datos.

```
def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0  
    return sum(numeros) / len(numeros)


lista_numeros = [10, 20, 30, 40, 50]
resultado = promedio_lista(lista_numeros)
print("El promedio de los números es:", resultado)
```

* Construir una función que reciba como parámetro una lista de datos numéricos y retorne el promedio de los datos pares.

```
def promedio_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    if len(pares) == 0:
        return 0
    return sum(pares) / len(pares)


lista_numeros = [10, 15, 20, 25, 30]
resultado = promedio_pares(lista_numeros)
print("El promedio de los números pares es:", resultado)
```