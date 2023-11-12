a = ['Pikachu', 'Bulbasaur', 'Charmander','wisin','Raichu','mierda']
b = ['Pikachu', 'Pichu', 'Raichu', 'Squirtle', 'popo', 'charmilion']

n = len(a)
m = len(b)
k = 0

if m <= n:
    for i in b:
        if i not in a:
            k += 1 
if n < m:
    for i in a:
        if i not in b:
            k += 1
print(k)
