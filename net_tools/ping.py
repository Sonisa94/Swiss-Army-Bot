import os
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def ping(destino, output_filename):

    comando = f"ping -c 1 {destino} > {output_filename}.txt" # El parámetro '-c 4' limita a 4 intentos en sistemas Unix

    print("\nEjecutando ping...\n")

    # Ejecutar el comando y mostrar la salida
    resultado = os.system(comando)

    # Evaluar el resultado del ping
    if resultado == 0:
        print(f"\nEl ping a {destino} fue exitoso.\n")
        return 0
    else:
        print(f"\nNo se pudo alcanzar {destino}. Verifique la dirección e inténtelo nuevamente.\n")
        return -1

if __name__ == "__main__":
    ping('8.8.8.8')
