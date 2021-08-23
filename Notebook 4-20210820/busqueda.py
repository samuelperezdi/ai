class Nodo:
    
    # Clase para crear los nodos
    
    def __init__(self, estado, madre, accion, costo_camino, codigo):
        self.estado = estado
        self.madre = madre
        self.accion = accion
        self.costo_camino = costo_camino
        self.codigo = codigo
        
def nodo_hijo(problema, madre, accion):
    
    # Función para crear un nuevo nodo
    # Input: problema, que es un objeto de clase ocho_reinas
    #        madre, que es un nodo,
    #        accion, que es una acción que da lugar al estado del nuevo nodo
    # Output: nodo
    
    estado = problema.transicion(madre.estado, accion)
    costo_camino = madre.costo_camino + problema.costo(madre.estado, accion)
    codigo = problema.codigo(estado)
    return Nodo(estado, madre, accion, costo_camino, codigo)


def breadth_first_search(problema):
    estado = problema.estado_inicial
    if problema.test_objetivo(estado):
        return estado
    frontera = [estado]
    while len(frontera) > 0:
        estado = frontera.pop(0)
        acciones = problema.acciones_aplicables(estado)
        for a in acciones:
            hijo = problema.transicion(estado, a)
            if problema.test_objetivo(hijo):
                return hijo
            frontera.append(hijo)
    return None