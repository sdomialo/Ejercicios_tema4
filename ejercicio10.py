class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_nivel(raiz, nivel):
    if raiz is None:
        return 0
    if nivel == 0:
        return 1
    return (contar_nodos_nivel(raiz.izquierda, nivel-1) +
            contar_nodos_nivel(raiz.derecha, nivel-1))

def nivel_completo(raiz, nivel):
    if raiz is None:
        return False
    if nivel == 0:
        return True
    if nivel == 1:
        return raiz.izquierda is not None and raiz.derecha is not None
    return (nivel_completo(raiz.izquierda, nivel-1) and
            nivel_completo(raiz.derecha, nivel-1))

def nodos_faltantes(raiz, nivel):
    if raiz is None:
        return 0
    if nivel == 0:
        return 0
    if nivel == 1:
        if raiz.izquierda is None:
            return 1
        if raiz.derecha is None:
            return 1
        return 0
    return (nodos_faltantes(raiz.izquierda, nivel-1) +
            nodos_faltantes(raiz.derecha, nivel-1))

# Ejemplo de uso
# Crear el árbol de ejemplo
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)

nivel = 2

# Calcular el número de nodos en el nivel dado
num_nodos = contar_nodos_nivel(raiz, nivel)
print(f"El número de nodos en el nivel {nivel} es: {num_nodos}")

# Determinar si el nivel del árbol está completo
completo = nivel_completo(raiz, nivel)
if completo:
    print(f"El nivel {nivel} del árbol está completo")
else:
    print(f"El nivel {nivel} del árbol no está completo")

# Calcular cuántos nodos faltan para completar el nivel
nodos_faltantes = nodos_faltantes(raiz, nivel)
print(f"El número de nodos faltantes en el nivel {nivel} es: {nodos_faltantes}")