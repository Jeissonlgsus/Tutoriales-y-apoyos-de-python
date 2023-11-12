    #numero = input("ingrese un número: ")
lista = list(range(1,10))
    #print(lista)
# es necesario ver que que una lista es un elemento con varios elementos, se determina con corchetes
# por otro lado, el código "list()" convierte una variable en lista, asi como "int()" transforma en entero.
# la función "range(a,b)" me da valores ordenados de un valor "a" hasta un valor "b-1".
    #print(numero in lista)
# "in" determina si un elemento pertenece o no a una lista
lista.append(10)
print(lista)
# la funcion "append" sirve para colocar valores a una lista de manera unitaria
# aunque la funcion "extend" hace lo mismo, esta permite agregar más elementos por medio de tuplas
    #lista.extend((11,12))
    #print(lista)
# para insertar elementos en una posicion dada, usamos la funcion "insert(a,b)" donde "a" es la posicion y "b" el elemento a agregar
    #lista.insert(1,69)
    #print(lista)
    #lista.insert(len(lista), 71)
    #print(lista)
# la funcion "len" nos da la cantidad de elementos que tiene la lista, por tanto al usarlo en la función "insert" manda el nuevo elemento 
# en la última posición
    #lista.pop(0)
    #print(lista)
# la función "pop" elimina el elemento de la lista con el indice especificado, sin embargo, para quitar un elemento sin importar la posicion, usamos la función "remove"
    #lista.remove(10)
    #print(lista)
# finalmente, para borrar todos los elementos de la lista, usamos la función "clear"
    #lista.clear()
colores = ['amarillo', 'verde', 'azul', 'rojo', 'azul']
print(colores)
# la función "sort" sirve para ordenar una lista en el orden alfabético
colores.sort()
print(colores)
# con el parametro "reverse = True" invierte el orden de la lista, no olvidemos que "True" al ser una constante, debe llevar MAYUSCULA
colores.sort(reverse = True)
print(colores)
# para obtener el indice de un elemento, usamos la funcion "index" 
a = colores.index("azul") 
print(a)
# para saber cuantas veces esta un elemento en la lista, usamos la función "count"
b = colores.count("azul")
print(b)
