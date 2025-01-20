import os
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def wakeonlan(destino, output_filename="Default"):

    comando = f"wakeonlan {destino} > {output_filename}.txt"
    print("\nEjecutando wakeonlan...\n")

    # Ejecutar el comando y mostrar la salida
    resultado = os.system(comando)


    if resultado == 0:
        print(f"\nEl wakeonlan a {destino} fue exitoso.\n")
        return 0
    else:
        print(f"\nNo se pudo alcanzar {destino}. Verifique la dirección e inténtelo nuevamente.\n")
        return -1

if __name__ == "__main__":
    wakeonlan('00:e0:6c:68:2d:e7')
