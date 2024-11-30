import random
import os


class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validar_numero(self, numero):
        if numero < self.numero_secreto:
            return 1  # Número menor
        elif numero == self.numero_secreto:
            return 2  # Número correcto
        else:
            return 3  # Número mayor

    def registrar_intento(self):
        self.intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidas_jugadas = 0
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0

    def actualizar_historial(self, ganar):
        self.partidas_jugadas += 1
        if ganar == 1:
            self.partidas_ganadas += 1
        else:
            self.partidas_perdidas += 1

    def mostrar_estadisticas(self):
        ganadas_pct = (self.partidas_ganadas / self.partidas_jugadas * 100) if self.partidas_jugadas > 0 else 0
        perdidas_pct = (self.partidas_perdidas / self.partidas_jugadas * 100) if self.partidas_jugadas > 0 else 0
        print(f"""
Estadísticas del jugador {self.nombre}:
- Partidas jugadas: {self.partidas_jugadas}
- Partidas ganadas: {ganadas_pct:.2f}%
- Partidas perdidas: {perdidas_pct:.2f}%
""")


def cargar_estadisticas(nombre):
    archivo = f"{nombre}.txt"
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            datos = f.read().strip().split(";")
            jugador = Jugador(nombre)
            jugador.partidas_jugadas = int(datos[0])
            jugador.partidas_ganadas = int(datos[1])
            jugador.partidas_perdidas = int(datos[2])
            return jugador
    return Jugador(nombre)


def guardar_estadisticas(jugador):
    archivo = f"{jugador.nombre}.txt"
    with open(archivo, "w") as f:
        f.write(f"{jugador.partidas_jugadas};{jugador.partidas_ganadas};{jugador.partidas_perdidas}")


def menu():
    jugador = None
    while True:
        opcion = input("""
Elige una opción:
1. Jugar una nueva partida
2. Ver estadísticas
3. Salir
> """)
        if opcion == "1":
            nombre = input("Ingresa tu nombre: ")
            jugador = cargar_estadisticas(nombre)
            juego = JuegoAdivinanza()
            juego.reiniciar()
            stop = False
            while stop == False:
                numero = int(input("Adivina el número (entre 1 y 100): "))
                juego.registrar_intento()
                resultado = juego.validar_numero(numero)
                if resultado == 1:
                    print("El número es mayor, perdiste.")
                    jugador.actualizar_historial(2)
                elif resultado == 3:
                    print("El número es menor, ganaste.")
                    jugador.actualizar_historial(1)
                seguir = input("Ingrese 1 si desea dejar de jugar, ingrese cualquier otro número si desea volver a jugar: ")
                if seguir == "1" :
                    stop = True
            guardar_estadisticas(jugador)
        elif opcion == "2":
            if jugador:
                jugador.mostrar_estadisticas()
            else:
                print("Aún no has jugado ninguna partida. Juega primero para ver estadísticas.")
        elif opcion == "3":
            if jugador:
                guardar_estadisticas(jugador)
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("Por favor, elige una opción válida.")


menu()
