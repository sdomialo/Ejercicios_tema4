class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierda = None
        self.derecha = None

def insertar(raiz, nombre, es_heroe):
    if raiz is None:
        return Nodo(nombre, es_heroe)
    if nombre < raiz.nombre:
        raiz.izquierda = insertar(raiz.izquierda, nombre, es_heroe)
    else:
        raiz.derecha = insertar(raiz.derecha, nombre, es_heroe)
    return raiz

def listar_villanos(raiz):
    if raiz is not None:
        listar_villanos(raiz.izquierda)
        if not raiz.es_heroe:
            print(raiz.nombre)
        listar_villanos(raiz.derecha)

def listar_superheroes_con_c(raiz):
    if raiz is not None:
        listar_superheroes_con_c(raiz.izquierda)
        if raiz.nombre.startswith('C'):
            print(raiz.nombre)
        listar_superheroes_con_c(raiz.derecha)

def contar_superheroes(raiz):
    if raiz is None:
        return 0
    return 1 + contar_superheroes(raiz.izquierda) + contar_superheroes(raiz.derecha)

def buscar_y_modificar(raiz, nombre_viejo, nombre_nuevo):
    if raiz is None:
        return
    if raiz.nombre == nombre_viejo:
        raiz.nombre = nombre_nuevo
    buscar_y_modificar(raiz.izquierda, nombre_viejo, nombre_nuevo)
    buscar_y_modificar(raiz.derecha, nombre_viejo, nombre_nuevo)

def listar_superheroes_descendente(raiz):
    if raiz is not None:
        listar_superheroes_descendente(raiz.derecha)
        print(raiz.nombre)
        listar_superheroes_descendente(raiz.izquierda)

# Crear el árbol
arbol = None
arbol = insertar(arbol, "Iron Man", True)
arbol = insertar(arbol, "Captain America", True)
arbol = insertar(arbol, "Thor", True)
arbol = insertar(arbol, "Hulk", True)
arbol = insertar(arbol, "Black Widow", True)
arbol = insertar(arbol, "Loki", False)
arbol = insertar(arbol, "Thanos", False)
arbol = insertar(arbol, "Red Skull", False)
arbol = insertar(arbol, "Doctor Strange", True)

# Listar villanos ordenados alfabéticamente
print("Villanos ordenados alfabéticamente:")
listar_villanos(arbol)

# Mostrar superhéroes que empiezan con C
print("Superhéroes que empiezan con C:")
listar_superheroes_con_c(arbol)

# Determinar cuántos superhéroes hay en el árbol
cantidad_superheroes = contar_superheroes(arbol)
print("Cantidad de superhéroes:", cantidad_superheroes)

# Buscar y modificar el nombre de Doctor Strange
buscar_y_modificar(arbol, "Doctor Strange", "Doctor Strange (correcto)")

# Listar superhéroes en orden descendente
print("Superhéroes en orden descendente:")
listar_superheroes_descendente(arbol)