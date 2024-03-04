import pyautogui
import keyboard
import time
from threading import Thread


def click_button():
    button_image = 'ruta_de_la_imagen_del_boton.png'  # Reemplaza con la ruta de la imagen del botón
    button_position = pyautogui.locateOnScreen(button_image)

    if button_position:
        # Obtiene las coordenadas centrales del botón
        button_center_x, button_center_y = pyautogui.center(button_position)

        # Realiza el clic en el centro del botón
        pyautogui.click(button_center_x, button_center_y)
    else:
        print("No se pudo encontrar el botón en la pantalla.")


def monitor_hotkey():
    keyboard.add_hotkey('alt+f1', lambda: Thread(target=click_button).start())


if __name__ == "__main__":
    # Inicia la monitorización de la combinación de teclas en segundo plano
    monitor_thread = Thread(target=monitor_hotkey)
    monitor_thread.daemon = True
    monitor_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
