import os
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def dig(destino, output_filename="default"):

    comando = f"dig {destino} > {output_filename}.txt" 

    print("\nEjecutando dig...\n")

    # Ejecutar el comando y mostrar la salida
    resultado = os.system(comando)


    if resultado == 0:
        print(f"\nEl dig a {destino} fue exitoso.\n")
        return 0
    else:
        print(f"\nNo se pudo alcanzar {destino}. Verifique la dirección e inténtelo nuevamente.\n")
        return -1

if __name__ == "__main__":
    dig('8.8.8.8')
