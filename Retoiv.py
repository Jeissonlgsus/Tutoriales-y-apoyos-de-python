import json

EntradaJson= input("")
Entrada2= input("")

Ref = Entrada2.split(' ')
#Ref.sort()


x = EntradaJson

Json = json.loads(x)

c=[]

ListaRef=list(Ref)
Json2=list(Json)

n=0
for i in ListaRef:
  if ListaRef[n] in Json2:
    c.append(ListaRef[n])
  n+=1

k=0
l=0
for i in c:
  k+=Json[c[l]]
  l+=1

cadena = " ".join(c)

print(k) 
print(cadena)