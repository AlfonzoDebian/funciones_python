print("------------------------------------------------")
print("-Buscar un numero en conjunto. ")
print("------------------------------------------------")

def buscarDatos(datosABuscar, lista):
    r = False
    for i in lista:
        if i == datosABuscar:
            r = True
    return

datos = int(input("Numeros: "))
lista = [1, 2, 3, 4, 5,]
if buscarDatos(dato, lista):
    print("Lo encontre. ")
else:
    print("No lo encontre. ")


print("\nEso era...")