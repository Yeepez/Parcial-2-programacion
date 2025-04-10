from habitacion import HabitacionDoble, HabitacionTriple, HabitacionCuadruple  # Importamos las clases de habitaciones
from reserva import Reserva  # Importamos la clase Reserva

# Clase principal del Hotel
class Hotel:
    def _init_(self):
        self.habitaciones = []  # Lista de todas las habitaciones disponibles
        self.reservas = []  # Lista de reservas hechas
        self.generar_habitaciones()  # Generamos las habitaciones automáticamente al crear el hotel

    def generar_habitaciones(self):
        # Genera habitaciones para 5 pisos, con 6 habitaciones por piso
        for piso in range(1, 6):  # Pisos del 1 al 5
            for i in range(1, 7):  # 6 habitaciones por piso
                numero = piso * 100 + i  # Ejemplo: piso 2 habitación 3 => 203
                if i <= 2:
                    self.habitaciones.append(HabitacionDoble(numero, piso))
                elif i <= 4:
                    self.habitaciones.append(HabitacionTriple(numero, piso))
                else:
                    self.habitaciones.append(HabitacionCuadruple(numero, piso))

    def hacer_reserva(self, cantidad_huespedes, huespedes, fecha_entrada, fecha_salida):
        # Filtra habitaciones disponibles con la capacidad exacta requerida
        habitaciones_filtradas = [h for h in self.habitaciones if h.esta_disponible() and h._capacidad == cantidad_huespedes]
        if not habitaciones_filtradas:
            print(f"No hay habitaciones disponibles para {cantidad_huespedes} personas.")
            return None

        # Muestra habitaciones disponibles
        print("Habitaciones disponibles:")
        for idx, h in enumerate(habitaciones_filtradas):
            print(f"{idx+1}. {h}")

        # Solicita al usuario seleccionar una habitación por índice
        while True:
            try:
                seleccion = int(input("Seleccione una habitación (número de lista): "))
                if 1 <= seleccion <= len(habitaciones_filtradas):
                    break
                else:
                    print("Selección fuera de rango.")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

        habitacion = habitaciones_filtradas[seleccion - 1]  # Se obtiene la habitación seleccionada
        habitacion.reservar()  # Se marca como no disponible
        reserva = Reserva(habitacion, huespedes, fecha_entrada, fecha_salida)  # Se crea la reserva
        self.reservas.append(reserva)  # Se guarda en la lista de reservas
        return reserva

    def mostrar_reservas(self):
    # Filtra solo las reservas activas
        reservas_activas = [r for r in self.reservas if r.activa]
        if not reservas_activas:
            print("No hay reservas activas.")
        else:
            for r in reservas_activas:
                print(r)


    def cancelar_reserva(self, numero_habitacion):
         # Cancela la reserva activa de una habitación específica
        for r in self.reservas:
            if r.habitacion._numero == numero_habitacion and r.activa:
                r.cancelar()  # Marca la reserva como inactiva y libera la habitación
            return True
            print("No se encontró ninguna reserva activa para esa habitación.")  # Mensaje si no hay reserva activa
        return False  # Retorna False si no se pudo cancelar

    def mostrar_disponibles(self):
        # Muestra todas las habitaciones que están disponibles actualmente
        for h in self.habitaciones:
            if h.esta_disponible():
                print(h)


