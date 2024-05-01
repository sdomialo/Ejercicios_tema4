class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    elif valor < raiz.valor:
        raiz.izquierda = insertar(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izquierda) + contar_nodos(raiz.derecha)

def barrido_ordenado(raiz):
    if raiz is not None:
        barrido_ordenado(raiz.izquierda)
        print(raiz.valor)
        barrido_ordenado(raiz.derecha)

# Crear el árbol de superhéroes
arbol_superheroes = None
arbol_superheroes = insertar(arbol_superheroes, "Spider-Man")
arbol_superheroes = insertar(arbol_superheroes, "Iron Man")
arbol_superheroes = insertar(arbol_superheroes, "Captain America")
# Agregar más superhéroes si es necesario

# Crear el árbol de villanos
arbol_villanos = None
arbol_villanos = insertar(arbol_villanos, "Thanos")
arbol_villanos = insertar(arbol_villanos, "Joker")
arbol_villanos = insertar(arbol_villanos, "Loki")
# Agregar más villanos si es necesario

# Determinar cuántos nodos tiene cada árbol
num_nodos_superheroes = contar_nodos(arbol_superheroes)
num_nodos_villanos = contar_nodos(arbol_villanos)

# Realizar el barrido ordenado alfabéticamente de cada árbol
print("Superhéroes:")
barrido_ordenado(arbol_superheroes)

print("Villanos:")
barrido_ordenado(arbol_villanos)