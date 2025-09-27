
import random

# =========================
# CLASES
# =========================
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre


class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.max_vida = random.randint(150, 400)
        self.vida_actual = self.max_vida

    def recuperar(self):
        self.vida_actual = self.max_vida


# =========================
# VARIABLES GLOBALES
# =========================
entrenador1 = None
pokemon1 = None
entrenador2 = None
pokemon2 = None

ganadas = 0
perdidas = 0


# =========================
# FUNCIONES
# =========================
def crearEntrenadorPokemon(num):
    global entrenador1, pokemon1, entrenador2, pokemon2

    nombre_entrenador = input("Ingrese nombre del entrenador " + str(num) + ": ")
    nombre_pokemon = input("Ingrese nombre del pokemon " + str(num) + ": ")

    if num == 1:
        entrenador1 = Entrenador(nombre_entrenador)
        pokemon1 = Pokemon(nombre_pokemon)
        print("\nTu pokemon ha sido creado con estas estadísticas:")
        print("Nombre:", pokemon1.nombre)
        print("Ataque máximo:", pokemon1.max_ataque)
        print("Vida máxima:", pokemon1.max_vida, "\n")
    else:
        entrenador2 = Entrenador(nombre_entrenador)
        pokemon2 = Pokemon(nombre_pokemon)
        print("\nEl pokemon rival ha sido creado con estas estadísticas:")
        print("Nombre:", pokemon2.nombre)
        print("Ataque máximo:", pokemon2.max_ataque)
        print("Vida máxima:", pokemon2.max_vida, "\n")


def valorDeAtaque(num):
    if num == 1:
        return random.randint(0, pokemon1.max_ataque)
    else:
        return random.randint(0, pokemon2.max_ataque)


def defender(num, ataque):
    dado = random.randint(1, 6)
    if dado == 6:
        ataque = 0  # se anuló el ataque

    if num == 1:
        pokemon1.vida_actual = pokemon1.vida_actual - ataque
        return pokemon1.vida_actual
    else:
        pokemon2.vida_actual = pokemon2.vida_actual - ataque
        return pokemon2.vida_actual


# =========================
# PROGRAMA PRINCIPAL
# =========================
print("=== JUEGO DE PELEA POKEMON ===\n")

crearEntrenadorPokemon(1)  # Crear mi entrenador y pokemon

while True:
    print("Menú: ")
    print("P = Pelear")
    print("F = Finalizar")
    opcion = input("Elija una opción: ").upper()

    if opcion == "F":
        print("\n=== FIN DEL JUEGO ===")
        print("Entrenador:", entrenador1.nombre)
        print("Pokemon:", pokemon1.nombre)
        print("Ataque máximo:", pokemon1.max_ataque)
        print("Vida máxima:", pokemon1.max_vida)
        print("Encuentros ganados:", ganadas)
        print("Encuentros perdidos:", perdidas)
        break

    elif opcion == "P":
        crearEntrenadorPokemon(2)
        pokemon1.recuperar()
        pokemon2.recuperar()

        turno = 1  # empieza jugador1 siempre

        while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
            if turno == 1:
                ataque = valorDeAtaque(1)
                vida = defender(2, ataque)
                print(entrenador1.nombre, "con", pokemon1.nombre,
                      "atacó con", ataque, "puntos.")
                print("Vida de", pokemon2.nombre, ":", vida, "\n")
                turno = 2
            else:
                ataque = valorDeAtaque(2)
                vida = defender(1, ataque)
                print(entrenador2.nombre, "con", pokemon2.nombre,
                      "atacó con", ataque, "puntos.")
                print("Vida de", pokemon1.nombre, ":", vida, "\n")
                turno = 1

        if pokemon1.vida_actual <= 0:
            print("Ganador:", entrenador2.nombre, "con su pokemon", pokemon2.nombre, "\n")
            perdidas = perdidas + 1
        else:
            print("Ganador:", entrenador1.nombre, "con su pokemon", pokemon1.nombre, "\n")
            ganadas = ganadas + 1
    else:
        print("Opción incorrecta. Intente de nuevo.\n")
