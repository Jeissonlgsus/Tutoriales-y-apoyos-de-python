def obtener_todos(listainicial):

    listafinal = []
    for i in listainicial:
        if i not in listafinal:
            listafinal.append(i)
    
    print(listafinal)

def obtener_coincidencia(poslista,pokemonlista,pokemonbuscado):
    d = []
    for i in poslista:
        if pokemonlista[i] == pokemonbuscado:
            d.append(i)

    print(d)

def obtener_pokemon_diferentes(pokemonusuario1,pokemonusuario2):
        
        c = []
        for i in pokemonusuario1:
            if i not in pokemonusuario2:
                c.append(i)

        print(c)

def obtener_numero_intercambios(pokemonusuario1,pokemonusuario2):
        n = len(pokemonusuario1)
        m = len(pokemonusuario2)
        k = 0

        if m <= n:
            for i in pokemonusuario2:
                if i not in pokemonusuario1:
                    k += 1 
        if n < m:
            for i in pokemonusuario1:
                if i not in pokemonusuario2:
                    k += 1
        print(k)
