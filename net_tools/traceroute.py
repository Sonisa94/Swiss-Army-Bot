import os
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def traceroute(destino, output_filename="Default"):

    comando = f"traceroute {destino} > {output_filename}.txt"
    print("\nEjecutando traceroute...\n")

    # Ejecutar el comando y mostrar la salida
    resultado = os.system(comando)


    if resultado == 0:
        print(f"\nEl traceroute a {destino} fue exitoso.\n")
        return 0
    else:
        print(f"\nNo se pudo alcanzar {destino}. Verifique la dirección e inténtelo nuevamente.\n")
        return -1

if __name__ == "__main__":
    traceroute('8.8.8.8')
