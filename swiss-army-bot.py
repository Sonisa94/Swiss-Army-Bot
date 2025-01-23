from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio
import os

from net_tools import *
from utils import generar_cadena
from http_tools import *
from user_management import *

#Obtener el token de tu bot desde variable de entorno
TOKEN = os.environ.get("SWISSARMYTOKEN")


#Comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Hola! Soy tu bot. Si quieres tener acceso completo a mis funciones, por favor introduce /request y en la mayor brevedad posible tendras acceso. Gracias!"
    )

#Comando /ping
async def handle_ping(update: Update, context: CallbackContext):
    if context.args:
        #Obtener dominio o IP proporcionado por el usuario
        target = context.args[0]
        output_filename = generar_cadena()
        result = ping(target, output_filename)
        with open(output_filename + '.txt', 'r') as file:
            contenido = file.read()
        os.remove(output_filename + '.txt')
        #await update.message.reply_text(f"Ping a {target}:\n{result}")
        await update.message.reply_text(contenido)

    else:
        await update.message.reply_text("Por favor, proporciona una dirección IP o dominio para hacer ping. Ejemplo: /ping google.com")

#Comando /dig
async def handle_dig(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            target= context.args[0]
            output_filename = generar_cadena()
            result = dig(target, output_filename)
            with open(output_filename + '.txt', 'r') as file:
                contenido = file.read()
            os.remove(output_filename + '.txt')
            await update.message.reply_text(contenido)
        else:
            await update.message.reply_text("Por favor, proporciona una dirección IP o dominio para hacer dig. Ejemplo: /dig google.com")
    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /nslookup
async def handle_nslookup(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            target= context.args[0]
            output_filename = generar_cadena()
            result = nslookup(target, output_filename)
            with open(output_filename + '.txt', 'r') as file:
                contenido = file.read()
            os.remove(output_filename + '.txt')
            await update.message.reply_text(contenido)
        else:
            await update.message.reply_text("Por favor, proporciona una dirección IP o dominio para hacer dig. Ejemplo: /nslookup google.com")
    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /traceroute
async def handle_traceroute(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            target= context.args[0]
            output_filename = generar_cadena()
            result = traceroute(target, output_filename)
            with open(output_filename + '.txt', 'r') as file:
                contenido = file.read()
            os.remove(output_filename + '.txt')
            await update.message.reply_text(contenido)
        else:
            await update.message.reply_text("Por favor, proporciona una dirección IP o dominio")
    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /wakeonlan
async def handle_wakeonlan(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            target= context.args[0]
            output_filename = generar_cadena()
            result = wakeonlan(target, output_filename)
            with open(output_filename + '.txt', 'r') as file:
                contenido = file.read()
            os.remove(output_filename + '.txt')
            await update.message.reply_text(contenido)
        else:
            await update.message.reply_text("Por favor, proporciona una dirección MAC")
    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /get
async def handle_get(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            url= context.args[0]
            output_filename = generar_cadena()
            result = get(url, output_filename)
            with open(result, "rb") as file:
                await update.message.reply_document(document=file)
            os.remove(result)
        else:
            await update.message.reply_text("Por favor, proporciona una URL")

    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /post
async def handle_post(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            url= context.args[0]
            output_filename = generar_cadena()
            result = post(url, output_filename)
            try:
                if result != 0:
                    with open(result, "rb") as file:
                        await update.message.reply_document(document=file)
                    os.remove(result)
            except Exception:
                await update.message.reply_text("Metodo no soportado por esa URL")
        else:
            await update.message.reply_text("Por favor, proporciona una URL")

    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /put
async def handle_put(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            url= context.args[0]
            output_filename = generar_cadena()
            result = post(url, output_filename)
            try:
                if result != 0:
                    with open(result, "rb") as file:
                        await update.message.reply_document(document=file)
                    os.remove(result)
            except Exception:
                await update.message.reply_text("Metodo no soportado por esa URL")
        else:
            await update.message.reply_text("Por favor, proporciona una URL")

    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /options
async def handle_options(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            url= context.args[0]
            output_filename = generar_cadena()
            result = options(url, output_filename)
            try:
                if result != 0:
                    with open(result, "rb") as file:
                        await update.message.reply_document(document=file)
                    os.remove(result)
            except Exception:
                await update.message.reply_text("Metodo no soportado por esa URL")
        else:
            await update.message.reply_text("Por favor, proporciona una URL")
    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /patch
async def handle_patch(update: Update, context: CallbackContext):
    user = update.message.from_user
    if check_whitelisted(user.id):
        if context.args:
            url= context.args[0]
            output_filename = generar_cadena()
            result = patch(url, output_filename)
            try:
                if result != 0:
                    with open(result, "rb") as file:
                        await update.message.reply_document(document=file)
                    os.remove(result)
            except Exception:
                await update.message.reply_text("Metodo no soportado por esa URL")
        else:
            await update.message.reply_text("Por favor, proporciona una URL")
    else:
        await update.message.reply_text("Sin autorizacion. Por favor, solicita permiso con el comando /request")

#Comando /request
async def handle_request(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user

    usuarios_registrados = cargar_user_register_request()
    if user.id not in usuarios_registrados:
        usuarios_registrados.append(user.id)
        guardar_user_register_request(usuarios_registrados)
        print(f"Usuario registrado: {user.first_name} , ID: {user.id}")
        await update.message.reply_text(f"Hola {user.first_name}! Gracias por usarnos :D, su solicitud sera revisada.")
    else:
        await update.message.reply_text(f"Hola {user.first_name}! Su solicitud se esta revisando.")



#Comando /portscanning
async def handle_portscanning(update: Update, context: CallbackContext):
    if context.args:
        #Obtener dominio o IP proporcionado por el usuario
        target = context.args[0]
        ports = context.args[1]
        output_filename = generar_cadena()
        result = portscanning(target, ports, output_filename)
        with open(output_filename + '.txt', 'r') as file:
            contenido = file.read()
        os.remove(output_filename + '.txt')
        #await update.message.reply_text(f"Ping a {target}:\n{result}")
        await update.message.reply_text(contenido)

    else:
        await update.message.reply_text("Por favor, proporciona una dirección IP o dominio para hacer ping.")



#Comando personalizado /echo
async def echo(update: Update, context: CallbackContext):
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("Por favor, escribe un mensaje con /echo ")


#Respuesta a otros mensajes
async def handle_message(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Lo siento, no lo he entendido. Usa /help para ver los comandos disponibles."
    )

#Comando /help
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Aquí tienes algunos comandos que puedes usar: \n"
        #General Management
        "/start - Inicia el bot \n"
        "/help - Muestra el mensaje de ayuda \n"
        "/echo [mensaje] - Mensaje a repetir \n"
        "/request - Registro usuario \n"
        #Net Tools
        "/ping [IP /Host]- Lanzar ping a IP/ Dominio \n"
        "/dig [IP/Host]- Resolver dominio en IP o viceversa \n"
        "/nslookup [IP/Host]-Resolver nombres de dominio en IP y viceversa \n"
        "/traceroute [IP/Host]- Muestra la ruta que siguen los datos a través de internet \n"
        "/wakeonlan [MAC]- Encender de manera remota a través de una red local o internet \n"
        #HTTP Tools
        "/get [URL]- Para pedir recursos HTTP Get \n"
        "/post [URL]- Para pedir recursos HTTP Post \n"
        "/put [URL]- Para pedir recursos HTTP Put \n"
        "/options [URL]- Para pedir recursos HTTP Options \n"
        "/patch [URL]- Para pedir recursos HTTP Update \n"
        "/portscanning [IP/HOST]- Para verificar puertos"



    )



#Comando personalizado /echo
async def echo(update: Update, context: CallbackContext):
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("Por favor, escribe un mensaje con /echo ")
#Respuesta a otros mensajes
async def handle_message(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Lo siento, no lo he entendido. Usa /help para ver los comandos disponibles."
    )


#Configuracion del bot
def main():
    #Crear aplicacion
    application = Application.builder().token(TOKEN).build()

    #Management
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("request", handle_request))

    #Net Tools
    application.add_handler(CommandHandler("ping", handle_ping))
    application.add_handler(CommandHandler("dig", handle_dig))
    application.add_handler(CommandHandler("nslookup", handle_nslookup))
    application.add_handler(CommandHandler("traceroute", handle_traceroute))
    application.add_handler(CommandHandler("wakeonlan", handle_wakeonlan))
    application.add_handler(CommandHandler("portscanning", handle_portscanning))

    #HTTP Tools
    application.add_handler(CommandHandler("get", handle_get))
    application.add_handler(CommandHandler("post", handle_post))
    application.add_handler(CommandHandler("put", handle_put))
    application.add_handler(CommandHandler("options", handle_options))
    application.add_handler(CommandHandler("patch", handle_patch))


    #Manejador generico para mensajes que no son comandos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    #Ejecucion del bot
    print("Ejecutando")
    application.run_polling()
if __name__ == "__main__":
    main()
