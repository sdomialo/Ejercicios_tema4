class Jedi:
    def __init__(self, nombre, especie, anio_nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.anio_nacimiento = anio_nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros

def crear_arbol_nombre(jedis):
    arbol_nombre = {}
    for jedi in jedis:
        arbol_nombre[jedi.nombre] = jedi
    return arbol_nombre

def crear_arbol_ranking(jedis):
    arbol_ranking = {}
    for jedi in jedis:
        if jedi.ranking not in arbol_ranking:
            arbol_ranking[jedi.ranking] = []
        arbol_ranking[jedi.ranking].append(jedi)
    return arbol_ranking

def crear_arbol_especie(jedis):
    arbol_especie = {}
    for jedi in jedis:
        if jedi.especie not in arbol_especie:
            arbol_especie[jedi.especie] = []
        arbol_especie[jedi.especie].append(jedi)
    return arbol_especie

def barrido_inorden_nombre(arbol_nombre):
    for nombre, jedi in sorted(arbol_nombre.items()):
        print(nombre, jedi.ranking)

def barrido_inorden_ranking(arbol_ranking):
    for ranking, jedis in sorted(arbol_ranking.items()):
        for jedi in jedis:
            print(jedi.nombre, ranking)

def barrido_por_nivel(arbol):
    niveles = [[(None, list(arbol.keys()))]]
    for nivel in niveles:
        for padre, hijos in nivel:
            for hijo in hijos:
                if isinstance(arbol[hijo], dict):
                    niveles.append([(hijo, list(arbol[hijo].keys()))])
                else:
                    print(hijo, arbol[hijo])

def mostrar_informacion_jedi(jedis, nombre):
    for jedi in jedis:
        if jedi.nombre == nombre:
            print("Nombre:", jedi.nombre)
            print("Especie:", jedi.especie)
            print("Año de nacimiento:", jedi.anio_nacimiento)
            print("Color de sable de luz:", jedi.color_sable)
            print("Ranking:", jedi.ranking)
            print("Maestros:", jedi.maestros)

def mostrar_toda_informacion_yoda_luke(jedis):
    mostrar_informacion_jedi(jedis, "Yoda")
    mostrar_informacion_jedi(jedis, "Luke Skywalker")

def listar_jedi_ranking(jedis, ranking):
    for jedi in jedis:
        if jedi.ranking == ranking:
            print(jedi.nombre)

def listar_jedi_color_sable(jedis, color_sable):
    for jedi in jedis:
        if color_sable in jedi.color_sable:
            print(jedi.nombre)

def listar_jedi_con_maestros(jedis):
    for jedi in jedis:
        if jedi.maestros:
            print(jedi.nombre)

def mostrar_jedi_especie(jedis, especies):
    for jedi in jedis:
        if jedi.especie in especies:
            print(jedi.nombre)

def listar_jedi_letra_a_o_guion(jedis):
    for jedi in jedis:
        if jedi.nombre.startswith("A") or "-" in jedi.nombre:
            print(jedi.nombre)