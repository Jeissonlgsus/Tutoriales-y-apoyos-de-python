# print("Ciclo for y ciclo while")
# comidas = ['arroz','pasta','banano','alverja', 'tocino']

# for comidas in comidas:
#     if comidas == 'banano':
#         #break
#         continue
#     print(comidas)
    # el comando "break" hace que el programa se detenga en el proceso
    # el comando "continue" hace que el proceso siga, evitando la parte que hizo que entrara al ciclo.
valor = input("ingrese un valor: ")
a = int(valor)
while  a <= 10:
    print(str(a)+" Es menor o igual a 10")
    a = a+1
    #tengamos en cuenta que si el "while" no tiene una variacion en su valor de verdad, se produce un ciclo infinito