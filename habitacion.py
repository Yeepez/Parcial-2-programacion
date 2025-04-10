# Clase base Habitacion
class Habitacion:
    def __init__(self, numero, piso, capacidad, costo):
        self._numero = numero  # Guarda el número único de la habitación (por ejemplo: 101)
        self._piso = piso  # Guarda en qué piso se encuentra la habitación
        self._capacidad = capacidad  # Capacidad máxima de personas en esta habitación
        self._costo = costo  # Costo por noche para esta habitación
        self._disponible = True  # Indica si la habitación está disponible (True) o reservada (False)

    def reservar(self):
        self._disponible = False  # Cambia el estado de la habitación a no disponible

    def cancelar(self):
        self._disponible = True  # Cambia el estado de la habitación a disponible nuevamente

    def esta_disponible(self):
        return self._disponible  # Retorna True si la habitación está disponible

    def __str__(self):
        # Retorna un string con información resumida de la habitación
        return f"Habitación {self._numero} - Piso {self._piso} - Capacidad: {self._capacidad} - Precio: ${self._costo} - Disponible: {self._disponible}"

# Clases hijas que heredan de Habitacion y definen capacidad y costo específico
class HabitacionDoble(Habitacion):
    def __init__(self, numero, piso):
        super().__init__(numero, piso, 2, 100000)  # Capacidad 2 personas, costo $100000 por noche

class HabitacionTriple(Habitacion):
    def __init__(self, numero, piso):
        super().__init__(numero, piso, 3, 150000)  # Capacidad 3 personas, costo $150000 por noche

class HabitacionCuadruple(Habitacion):
    def __init__(self, numero, piso):
        super().__init__(numero, piso, 4, 200000)  # Capacidad 4 personas, costo $200000 por noche




