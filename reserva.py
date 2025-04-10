from datetime import datetime  # Importamos datetime para trabajar con fechas

# Clase que representa una reserva
class Reserva:
    def __init__(self, habitacion, huespedes=[], fecha_entrada=None, fecha_salida=None):
        self.habitacion = habitacion  # Habitación que se reserva
        self.huespedes = huespedes  # Lista de objetos Huesped
        self.activa = True  # Estado de la reserva, activa por defecto
        self.fecha_entrada = fecha_entrada  # Fecha de entrada
        self.fecha_salida = fecha_salida  # Fecha de salida
        self.noches = (self.fecha_salida - self.fecha_entrada).days  # Cantidad de noches
        self.precio_total = self.habitacion._costo * self.noches  # Precio total = noches * costo por noche

    def cancelar(self):
        self.activa = False  # Cambia el estado de la reserva a inactiva
        self.habitacion.cancelar()  # Libera la habitación (la hace disponible)

    def __str__(self):
        # Retorna información legible sobre la reserva, incluyendo los nombres de los huéspedes
        nombres = ", ".join([h.nombre for h in self.huespedes])
        estado = "(Cancelada)" if not self.activa else ""
        return f"Reserva en habitación {self.habitacion._numero} para {nombres} - Del {self.fecha_entrada.date()} al {self.fecha_salida.date()} - Total: ${self.precio_total} {estado}"
    
    