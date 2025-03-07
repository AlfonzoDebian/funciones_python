def repetir_cadena(cadena, n):
    for _ in range(n):
        print(cadena)

texto = input("Ingrese una cadena de texto: ")
veces = int(input("Ingrese el número de veces que desea repetirla: "))


repetir_cadena(texto, veces)
