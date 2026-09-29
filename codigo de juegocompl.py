import random
import os

# Personajes
personajes = {
    "1": {"nombre": "El Tigre", "vida": 100, "fuerza": 20},
    "2": {"nombre": "El Toro", "vida": 120, "fuerza": 15},
    "3": {"nombre": "La Pantera", "vida": 90, "fuerza": 25}
}

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pelea(jugador, enemigo):
    vida_j = jugador["vida"]
    vida_e = enemigo["vida"]

    print("\n¡COMIENZA LA PELEA!")
    input("Presiona ENTER...")

    while vida_j > 0 and vida_e > 0:
        limpiar()

        print("========== PELEA ==========")
        print(f"{jugador['nombre']}: {vida_j} HP")
        print(f"{enemigo['nombre']}: {vida_e} HP")
        print("============================")
        print("1. Golpear")
        print("2. Patada")
        print("3. Defender")

        opcion = input("Elige: ")

        # Turno del jugador
        if opcion == "1":
            daño = random.randint(10, jugador["fuerza"])
            vida_e -= daño
            print(f"\n¡Golpeaste e hiciste {daño} de daño!")

        elif opcion == "2":
            daño = random.randint(15, jugador["fuerza"] + 5)
            vida_e -= daño
            print(f"\n¡Patada! Hiciste {daño} de daño.")

        elif opcion == "3":
            print("\n¡Te defendiste!")
        else:
            print("\nOpción incorrecta.")
            input("ENTER...")
            continue

        # Turno enemigo
        if vida_e > 0:
            ataque = random.randint(1, 3)

            if opcion == "3":
                daño = random.randint(2, 8)
            else:
                daño = random.randint(8, enemigo["fuerza"])

            vida_j -= daño
            print(f"{enemigo['nombre']} te hizo {daño} de daño.")

        input("\nENTER para continuar...")

    limpiar()

    if vida_j <= 0:
        print("💀 HAS PERDIDO")
    else:
        print("🏆 ¡HAS GANADO!")

    input("\nENTER para volver al menú...")


def main():
    while True:
        limpiar()

        print("==========================")
        print("       UFC PYTHON")
        print("==========================")
        print("1. Jugar")
        print("2. Ver personajes")
        print("3. Salir")

        opcion = input("\nElige: ")

        if opcion == "1":
            limpiar()
            print("ELIGE TU LUCHADOR\n")

            for numero, personaje in personajes.items():
                print(
                    f"{numero}. {personaje['nombre']} "
                    f"- HP: {personaje['vida']} "
                    f"- Fuerza: {personaje['fuerza']}"
                )

            eleccion = input("\nElige: ")

            if eleccion in personajes:
                jugador = personajes[eleccion]

                enemigos = [
                    p for n, p in personajes.items()
                    if n != eleccion
                ]

                enemigo = random.choice(enemigos)

                print(f"\nTu luchador: {jugador['nombre']}")
                print(f"Rival: {enemigo['nombre']}")
                input("ENTER para empezar...")

                pelea(jugador, enemigo)

        elif opcion == "2":
            limpiar()

            print("===== PERSONAJES =====")

            for personaje in personajes.values():
                print(f"\n{personaje['nombre']}")
                print(f"Vida: {personaje['vida']}")
                print(f"Fuerza: {personaje['fuerza']}")

            input("\nENTER para volver...")

        elif opcion == "3":
            print("\n¡Gracias por jugar!")
            break

        else:
            print("\nOpción incorrecta.")
            input("ENTER...")


main()
