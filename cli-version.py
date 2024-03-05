import pyautogui
import time
from pynput import keyboard
import argparse

def click_on_button(button_image_path):
    # Hacer una pausa antes de buscar la imagen
    time.sleep(1)

    # Intentar encontrar el botón en la captura de pantalla hasta 5 veces
    for _ in range(5):
        button_location = pyautogui.locateOnScreen(button_image_path)
        if button_location is not None:
            # El botón fue encontrado, realiza las acciones necesarias
            button_x, button_y = pyautogui.center(button_location)
            pyautogui.click(button_x, button_y)
            return True
        else:
            # Hacer una pausa antes de intentar nuevamente
            time.sleep(1)

    # Si no se encuentra después de varios intentos, mostrar un mensaje en la consola
    print("¡Botón no encontrado!")
    return False

def select_image():
    # Obtener la ruta de la imagen desde la línea de comandos
    parser = argparse.ArgumentParser(description='Auto Deslogeo')
    parser.add_argument('image_path', type=str, help='Ruta de la imagen del botón')
    args = parser.parse_args()
    return args.image_path

def on_press(key):
    if any([key == k for k in atajo_teclado]):
        teclas_presionadas.add(key)

        # Verificar si se presionaron todas las teclas del atajo
        if all([k in teclas_presionadas for k in atajo_teclado]):
            click_on_button(button_image_path=ruta_del_boton)
    else:
        teclas_presionadas.clear()

def on_release(key):
    if any([key == k for k in atajo_teclado]):
        teclas_presionadas.remove(key)

# Ruta inicial de la captura del botón
ruta_del_boton = 'img/boton.png'

# Definir el atajo de teclado (Alt + F1)
atajo_teclado = {keyboard.Key.alt}

# Variables para rastrear el estado de las teclas
teclas_presionadas = set()

# Obtener la ruta de la imagen desde la línea de comandos
ruta_del_boton = select_image()

# Iniciar la escucha de eventos de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print(f"Imagen seleccionada: {ruta_del_boton}")
    print("Presione Ctrl + C para salir.")
    listener.join()
