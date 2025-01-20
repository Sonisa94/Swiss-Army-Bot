import random
import string

def generar_cadena():
    #Define el conjunto de caracteres alfanumericos
    caracteres = string.ascii_letters + string.digits #Incluye letras mayusculas y minusculas, y digitos.

    #Genera una cadena de 20 caracteres aleatorios
    cadena = ''.join(random.choice(caracteres) for _ in range(20))

    return cadena

if __name__ == "__main__":
    cadena_aleatoria = generar_cadena()
    print(cadena_aleatoria)
