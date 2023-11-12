print("Condicionales")
a = input("ingrese un valor: ")
c = int(a)
b = input("ingrese otro valor: ")
d = int(b)
if c < d:
    print(str(d)+" es mayor que "+str(c))
else:
    print(str(c)+" es mayor que "+str(d))
# para tener en cuenta, cuando se hace las comparaciones con mayor o menos se hace de manera normal, si es necesario comparar por igualdad 
# usamos el "==" que es igualdad logica.
# tengamos en cuenta que siempre que no se cumpla la condicion inicial,el "if" rebota en el "else"
# color = input("ingrese un color: ")
# if color == "azul":
#     print("el color que escribiste es azul")
# elif color == "rojo":
#     print("el color que escribiste es rojo")
# else:
#     print("el color que escribiste no es azul ni rojo")
