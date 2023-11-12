C1=input()

ListaC1=list(C1)

Rango=range(1,len(ListaC1))

Salida1=[]
Salida2=[]

k=1

for i in Rango:
  y=i
  x=i-1
  if C1[y]==C1[x]:
     k+=1
  else:
    Salida1.append(ListaC1[x])
    Salida2.append(k)
    k=1


print(Salida1,Salida2)