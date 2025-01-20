from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os
import asyncio

from net_tools import *
from utils import generar_cadena

#Obtener el token de tu bot desde variable de entorno
TOKEN = os.environ.get("SWISSARMYTOKEN")


#Comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Hola! Soy tu bot. Preguntame lo que quieras!"
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

#Comando /nslookup
async def handle_nslookup(update: Update, context: CallbackContext):
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

#Comando /help
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Aquí tienes algunos comandos que puedes usar: \n"
        "/start - Inicia el bot \n"
        "/help - Muestra el mensaje de ayuda \n"
        "/echo [mensaje] - Mensaje a repetir \n"
        "/ping [IP /Dominio]- Lanzar ping a IP/ Dominio \n"
        "/dig [IP/Dominio]- Resolver dominio en IP o viceversa \n"
        "/nslookup [IP/Dominio]-Resolver nombres de dominio en IP y viceversa "
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

    #Añadir manejadores para comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("ping", handle_ping))
    application.add_handler(CommandHandler("dig", handle_dig))
    application.add_handler(CommandHandler("nslookup", handle_nslookup))

    #Manejador generico para mensajes que no son comandos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    #Ejecucion del bot
    print("Ejecutando")
    application.run_polling()
if __name__ == "__main__":
    main()
