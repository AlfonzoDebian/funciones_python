print("----------------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("----------------------------------------")

#Entrada
b = int(input("numeros a buscar: "))

a = [1, 2, 3, 4, 5]
r = False

for i in a:
    if i==b:
        print("Lo Encontre")
        r = True
if r == False:
    print("No hay nada")
pass


print("\nEso era...")