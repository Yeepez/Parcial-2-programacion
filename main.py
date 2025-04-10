from hotel import Hotel  # Importamos clase principal del sistema
from huesped import Huesped  # Importamos clase para registrar huéspedes
from datetime import datetime  # Manejamos fechas
import re  # Usamos expresiones regulares para validar entradas de texto

hotel = Hotel()  # Creamos instancia del hotel

# Menú principal de opciones del sistema
while True:
    print("\n1. Hacer reserva\n2. Mostrar reservas\n3. Cancelar reserva\n4. Ver habitaciones disponibles\n5. Salir")
    op = input("Seleccione una opción: ")

    if op == "1":  # Hacer una nueva reserva
        try:
            cantidad = int(input("Cantidad de huéspedes (2, 3 o 4): "))
            if cantidad not in [2, 3, 4]:
                print("Solo se permiten habitaciones para 2, 3 o 4 personas.")
                continue

            huespedes = []
            for i in range(cantidad):
                # Validamos nombre del huésped
                while True:
                    nombre = input(f"Nombre del huésped {i+1}: ")
                    if not re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+", nombre):
                        print("Nombre inválido. Solo letras y espacios.")
                    else:
                        break
                # Validamos identificación
                while True:
                    identificacion = input("ID: ")
                    if not identificacion.isdigit():
                        print("La ID debe contener solo números.")
                    else:
                        break
                # Validamos edad
                while True:
                    edad = input("Edad: ")
                    if not edad.isdigit():
                        print("La edad debe contener solo números.")
                    else:
                        break
                huespedes.append(Huesped(nombre, identificacion, int(edad)))  # Se guarda huésped

            # Validamos fechas de entrada y salida
            while True:
                entrada = input("Fecha de entrada (YYYY-MM-DD): ")
                salida = input("Fecha de salida (YYYY-MM-DD): ")
                try:
                    fecha_entrada = datetime.strptime(entrada, "%Y-%m-%d")
                    fecha_salida = datetime.strptime(salida, "%Y-%m-%d")
                    if fecha_salida <= fecha_entrada:
                        print("La fecha de salida debe ser posterior a la de entrada.")
                    else:
                        break
                except ValueError:
                    print("Formato de fecha incorrecto. Use YYYY-MM-DD.")

            # Se realiza la reserva y se muestra confirmación
            reserva = hotel.hacer_reserva(cantidad, huespedes, fecha_entrada, fecha_salida)
            if reserva:
                print("¡Reserva realizada!")
                print(f"Precio total: ${reserva.precio_total}")
            else:
                print("No se pudo realizar la reserva.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    elif op == "2":  # Mostrar todas las reservas
        hotel.mostrar_reservas()

    elif op == "3":  # Cancelar reserva por número de habitación
        try:
            num = int(input("Número de habitación a cancelar: "))
            if hotel.cancelar_reserva(num):
                print("Reserva cancelada.")
            else:
                print("No se encontró la reserva activa.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número de habitación.")

    elif op == "4":  # Ver habitaciones disponibles
        hotel.mostrar_disponibles()

    elif op == "5":  # Salir del sistema
        break

    else:
        print("Opción no válida. Intente de nuevo.")