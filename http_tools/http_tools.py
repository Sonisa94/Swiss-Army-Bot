import requests
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def get(url):
    # Ejecutar el comando y mostrar la salida
    response =requests.get(url)
    content_type = response.headers.get("Content-Type")

    # Comprobar el código de estado de la respuesta
    if response.status_code == 200:
        content_type = response.headers.get("Content-Type")
        if content_type == "application/json":
            print("La respuesta obtenida json")
        if content_type == "text/html":
            print("La respuesta obtenida text/html")
        if content_type == "text/plain":
            print("La respuesta obtenida text/plain")
        if content_type == "application/xml":
            print("La respuesta obtenida application/xml")
        if content_type == "image/png":
            print("La respuesta obtenida image/png")
        if content_type == "image/jpeg":
            print("La respuesta obtenida imagen/jpeg")
            #data = response.json()
            #print("Respuesta obtenida:", data)

        return response.status_code
    else:
        print(f"Error al realizar la petición. Código de estado: {response.status_code}")
        return response.status_code

if __name__ == "__main__":
    get('https://api.ipify.org/?format=json')
    get('https://api.ipify.org')
    get('https://as.com/')
    get('https://as01.epimg.net/img/comunes/fotos/fichas/equipos/small/19.png')
