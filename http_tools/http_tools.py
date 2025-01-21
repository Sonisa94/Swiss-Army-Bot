import requests
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

#Comando /get
def get(url, file_name='Default'):
    # Ejecutar el comando y mostrar la salida
    response =requests.get(url)
    content_type = response.headers.get("Content-Type")

    # Comprobar el código de estado de la respuesta
    if response.status_code == 200:
        if "application/json" in content_type:
            file_name += ".json"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"La respuesta obtenida es JSON y se guardó como {file_name}")
            return file_name

        elif "text/html" in content_type:
            file_name += ".html"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"La respuesta obtenida es HTML y se guardó como {file_name}")
            return file_name

        elif "text/plain" in content_type:
            file_name += ".txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"La respuesta obtenida es texto plano y se guardó como {file_name}")
            return file_name

        elif "application/xml" in content_type or "text/xml" in content_type:
            file_name += ".xml"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"La respuesta obtenida es XML y se guardó como {file_name}")
            return file_name

        elif "image/png" in content_type:
            file_name += ".png"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"La respuesta obtenida es una imagen PNG y se guardó como {file_name}")
            return file_name

        elif "image/jpeg" in content_type:
            file_name += ".jpeg"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"La respuesta obtenida es una imagen JPEG y se guardó como {file_name}")
            return file_name

        else:
            file_name += ".bin"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Tipo de contenido no reconocido. La respuesta se guardó como {file_name}")
            return file_name

#Comando /post
def post(url, file_name='Default'):
    # Ejecutar el comando y mostrar la salida
    response =requests.post(url)
    content_type = response.headers.get("Content-Type")
    try:
        # Comprobar el código de estado de la respuesta
        if response.status_code == 200:
            if "application/json" in content_type:
                file_name += ".json"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es JSON y se guardó como {file_name}")
                return file_name

            elif "text/html" in content_type:
                file_name += ".html"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es HTML y se guardó como {file_name}")
                return file_name

            elif "text/plain" in content_type:
                file_name += ".txt"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es texto plano y se guardó como {file_name}")
                return file_name

            elif "application/xml" in content_type or "text/xml" in content_type:
                file_name += ".xml"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es XML y se guardó como {file_name}")
                return file_name

            elif "image/png" in content_type:
                file_name += ".png"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen PNG y se guardó como {file_name}")
                return file_name

            elif "image/jpeg" in content_type:
                file_name += ".jpeg"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen JPEG y se guardó como {file_name}")
                return file_name

            else:
                file_name += ".bin"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"Tipo de contenido no reconocido. La respuesta se guardó como {file_name}")
                return file_name
    except Exception:
        print(f"Metodo no soportado para esta URL")
        return 0
#Comando /put
def put(url, file_name='Default'):
    # Ejecutar el comando y mostrar la salida
    response =requests.put(url)
    content_type = response.headers.get("Content-Type")
    try:
        # Comprobar el código de estado de la respuesta
        if response.status_code == 200:
            if "application/json" in content_type:
                file_name += ".json"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es JSON y se guardó como {file_name}")
                return file_name

            elif "text/html" in content_type:
                file_name += ".html"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es HTML y se guardó como {file_name}")
                return file_name

            elif "text/plain" in content_type:
                file_name += ".txt"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es texto plano y se guardó como {file_name}")
                return file_name

            elif "application/xml" in content_type or "text/xml" in content_type:
                file_name += ".xml"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es XML y se guardó como {file_name}")
                return file_name

            elif "image/png" in content_type:
                file_name += ".png"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen PNG y se guardó como {file_name}")
                return file_name

            elif "image/jpeg" in content_type:
                file_name += ".jpeg"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen JPEG y se guardó como {file_name}")
                return file_name

            else:
                file_name += ".bin"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"Tipo de contenido no reconocido. La respuesta se guardó como {file_name}")
                return file_name
    except Exception:
        print(f"Metodo no soportado para esta URL")
        return 0

#Comando/options
def options(url, file_name='Default'):
    # Ejecutar el comando y mostrar la salida
    response =requests.options(url)
    content_type = response.headers.get("Content-Type")
    try:
        # Comprobar el código de estado de la respuesta
        if response.status_code == 200:
            if "application/json" in content_type:
                file_name += ".json"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es JSON y se guardó como {file_name}")
                return file_name

            elif "text/html" in content_type:
                file_name += ".html"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es HTML y se guardó como {file_name}")
                return file_name

            elif "text/plain" in content_type:
                file_name += ".txt"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es texto plano y se guardó como {file_name}")
                return file_name

            elif "application/xml" in content_type or "text/xml" in content_type:
                file_name += ".xml"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es XML y se guardó como {file_name}")
                return file_name

            elif "image/png" in content_type:
                file_name += ".png"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen PNG y se guardó como {file_name}")
                return file_name

            elif "image/jpeg" in content_type:
                file_name += ".jpeg"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen JPEG y se guardó como {file_name}")
                return file_name

            else:
                file_name += ".bin"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"Tipo de contenido no reconocido. La respuesta se guardó como {file_name}")
                return file_name
    except Exception:
        print(f"Metodo no soportado para esta URL")
        return 0

#Comando /patch
def patch(url, file_name='Default'):
    # Ejecutar el comando y mostrar la salida
    response =requests.patch(url)
    content_type = response.headers.get("Content-Type")
    try:
        # Comprobar el código de estado de la respuesta
        if response.status_code == 200:
            if "application/json" in content_type:
                file_name += ".json"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es JSON y se guardó como {file_name}")
                return file_name

            elif "text/html" in content_type:
                file_name += ".html"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es HTML y se guardó como {file_name}")
                return file_name

            elif "text/plain" in content_type:
                file_name += ".txt"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es texto plano y se guardó como {file_name}")
                return file_name

            elif "application/xml" in content_type or "text/xml" in content_type:
                file_name += ".xml"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"La respuesta obtenida es XML y se guardó como {file_name}")
                return file_name

            elif "image/png" in content_type:
                file_name += ".png"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen PNG y se guardó como {file_name}")
                return file_name

            elif "image/jpeg" in content_type:
                file_name += ".jpeg"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"La respuesta obtenida es una imagen JPEG y se guardó como {file_name}")
                return file_name

            else:
                file_name += ".bin"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                print(f"Tipo de contenido no reconocido. La respuesta se guardó como {file_name}")
                return file_name
    except Exception:
        print(f"Metodo no soportado para esta URL")
        return 0
#Comando /shortener

if __name__ == "__main__":
    get('https://api.ipify.org/?format=json')
    get('https://api.ipify.org')
    get('https://as.com/')
    get('https://as01.epimg.net/img/comunes/fotos/fichas/equipos/small/19.png')
