import os
import platform
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import json

USER_REGISTER_ACCESS = "user_register_request.json"
USER_REGISTERED = "user_registered.json"

def cargar_user_register_request():
    if os.path.exists(USER_REGISTER_ACCESS):
        with open(USER_REGISTER_ACCESS, 'r') as f:
            return json.load(f)
    return []

def guardar_user_register_request(usuarios):
    with open(USER_REGISTER_ACCESS, 'w') as f:
        json.dump(usuarios, f)

def cargar_user_registered():
    if os.path.exists(USER_REGISTERED):
        with open(USER_REGISTERED, 'r') as f:
            return json.load(f)
    return []

def check_whitelisted(user_id):
    registered_users = cargar_user_registered()
    return user_id in registered_users
