myStr = "Jisus"
# print(dir(myStr))
# el codigo dir, nos ayuda a ver las diferentes funciones en las que aplica la variable
print(myStr.upper())
# tengamos en cuenta que las funciones se separan por un punto
print(myStr.count("s"))
# count cuenta cuantas veces se repite un caracter
print(myStr.find("s"))
# la funcion find me asociacada caracter a un numero empezando por la posicion 0
# con lo cual, solo lanza la posicion del primer caracter encontrado.
print(myStr[4])
# al colocar un numero entre llaves este entiende que se necesita el caracter 
# en la posicion dada
print("Mi nombre es " + myStr)
# cuando queremos unir dos "variables" es necesario el signo "+" pues lo que hace es concatenar (unir)
