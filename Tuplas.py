# recordemos que las tuplas son "listas" inmutables, en ella nos sepueden cambiar los elementos
x = (1,2,3,4,5,6)
    # meses = ('enero','febrero','marzo', 'abril','mayo','junio', 'julio', 'agosto','septiembre','octubre','noviembre','diciembre')
    # a = len(meses)
    # print(a)
# para acceder a los elementos de una tupla, al igual que en la lista, usamos los corchetes y el indice del elemento que queremos extraer
    #a = x[4]
    #print(a)
# cuando decimos que una tupla es inmutable, mientras que una lista si, hacemos referencia a lo siguiente
y = [1,2,3,4,5,6]
    #x[4] = 10
    # en este caso manda un error pues x es inmutable
y[4] = 9
    #en este caso no lo hace pues las listas si pueden cambiar sus elementos
print(x)
print(y)
# para tener en cuenta: 
    # el lenguaje usado, respeta las diferentes tabulaciones, es decir, no se pueden colocar en diferentes tabulaciones, 
    # los diferentes procesos que comparten la misma linea
        # y = [1,2,3,4,5,6]
        #     #x[4] = 10
        #     # en este caso manda un error pues x es inmutable
        #     y[4] = 9
        #     #en este caso no lo hace pues las listas si pueden cambiar sus elementos
        # print(x)
        # print(y)
        # EN ESTE ULTIMO CASO, EL PROGRAMA BOTA ERROR PUES y[4] PERTENECE AL MISMO PROCESO DE LA TUPLA y
        