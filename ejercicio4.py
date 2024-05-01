class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho

def obtener_hijo_derecho(nodo):
    if nodo is None or nodo.derecho is None:
        return None
    return nodo.derecho

def obtener_hijo_izquierdo(nodo):
    if nodo is None or nodo.izquierdo is None:
        return None
    return nodo.izquierdo

# Ejemplo de uso
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo1.izquierdo = nodo2
nodo1.derecho = nodo3

hijo_izquierdo = obtener_hijo_izquierdo(nodo1)
hijo_derecho = obtener_hijo_derecho(nodo1)

print("Hijo izquierdo:", hijo_izquierdo.valor if hijo_izquierdo else None)
print("Hijo derecho:", hijo_derecho.valor if hijo_derecho else None)