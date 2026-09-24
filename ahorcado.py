import random

palabras = ["python", "computadora", "programa", "teclado", "codigo", "repositorio"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 6

print("=== ¡JUEGO DEL AHORCADO! ===")

while intentos > 0:
    # Construir la palabra mostrando las letras adivinadas y guiones bajo para las faltantes
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "

    print(f"\nPalabra: {estado.strip()}")
    print(f"Te quedan {intentos} intentos.")

    # Verificar si el jugador ya completó la palabra
    if "_" not in estado:
        print("\n¡FELICIDADES! 🎉 ¡Adivinaste la palabra!")
        break

    # Pedir una letra al usuario
    letra_usuario = input("Ingresa una letra: ").lower()

    if len(letra_usuario) != 1 or not letra_usuario.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue

    if letra_usuario in letras_adivinadas:
        print("Ya intentaste esa letra. Prueba con otra.")
    elif letra_usuario in palabra_secreta:
        letras_adivinadas.append(letra_usuario)
        print("¡Correcto! La letra está en la palabra.")
    else:
        letras_adivinadas.append(letra_usuario)
        intentos -= 1
        print("Incorrecto. Pierdes un intento.")

if intentos == 0:
    print(f"\n¡Game Over! 💀 Te quedaste sin intentos. La palabra era: {palabra_secreta}")