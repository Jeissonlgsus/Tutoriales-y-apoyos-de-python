import json

entrada = input("ingrese productos y valores: ") #ingresa productos y sus puntos
entrada2 = input("ingrese lista para mercar: ") # ingresa productos de tu lista

productos = entrada2.split(' ')

j=json.loads(entrada)

print(j)
print(productos)