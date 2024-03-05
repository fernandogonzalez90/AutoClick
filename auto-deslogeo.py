import pyautogui
import time
from pynput import keyboard
from tkinter import Tk, filedialog, Button, Label
import tkinter as tk
import pystray
from pystray import MenuItem as item
from PIL import Image
# Carga el modulo para registrar la app en inicio del sistema.
from reg import add_to_startup, is_app_in_startup

if not is_app_in_startup():
    add_to_startup()

class AppTray:
    def __init__(self, on_select_image_callback, on_exit_callback):
        self.on_select_image_callback = on_select_image_callback
        self.on_exit_callback = on_exit_callback

        # Configura el ícono de la bandeja de notificaciones
        self.image = Image.open("img/icon.ico")  # Ajusta el nombre de tu archivo de ícono
        self.menu = (item('Cargar Imagen', self.on_select_image), item('Salir', self.on_exit))
        self.icon = pystray.Icon("app_icon", self.image, "App Name", self.menu)

    def on_select_image(self, icon, item):
        # Llama a la función de carga de imagen cuando se selecciona "Cargar Imagen" en la bandeja de notificaciones
        self.on_select_image_callback()

    def on_exit(self, icon, item):
        # Llama a la función de salir cuando se selecciona "Salir" en la bandeja de notificaciones
        self.on_exit_callback()
        icon.stop()

    def run_tray(self):
        # Agrega el ícono a la bandeja de notificaciones
        self.icon.run()

def set_not_found_label(text):
    not_found_label.config(text=text)

def click_on_button(button_image_path):
    # Hacer una pausa antes de buscar la imagen
    time.sleep(1)

    # Intentar encontrar el botón en la captura de pantalla hasta 5 veces
    for _ in range(20):
        try:
            button_location = pyautogui.locateOnScreen(button_image_path, confidence=0.7)
            if button_location is not None:
                # El botón fue encontrado, realiza las acciones necesarias
                button_x, button_y = pyautogui.center(button_location)
                pyautogui.click(button_x, button_y)
                return True
            else:
                # Hacer una pausa antes de intentar nuevamente
                time.sleep(2)
        except Exception as e:
            print(f'Error al buscar la imagen {button_image_path}')

            print(f"Error al buscar la imagen: {e}")

    # Si no se encuentra después de varios intentos, mostrar un mensaje en el label
    not_found_label.config(text="¡Botón no encontrado!")

    return False

def select_image():
    # Abrir el cuadro de diálogo para seleccionar archivo y obtener la ruta de la imagen
    file_path = filedialog.askopenfilename(
        title="Seleccione la imagen del botón",
        filetypes=[("Image files", (".png", ".jpg", ".jpeg"))]
    )

    return file_path

ruta_del_boton = 'img/logout.png'
def on_select_image():
    global ruta_del_boton
    nueva_ruta = select_image()
    if nueva_ruta:
        ruta_del_boton = nueva_ruta
        message_label.config(text=f"Imagen seleccionada:\n{ruta_del_boton}")
        not_found_label.config(text="")  # Limpiar el mensaje de "no encontrado"



root = tk.Tk()
root.title("Auto Deslogeo")
root.geometry("400x200")

message_label = Label(root, text=f"Imagen seleccionada:\n{ruta_del_boton}")
message_label.pack(pady=10)

not_found_label = Label(root, text="")
not_found_label.pack(pady=10)

select_image_button = Button(root, text="Seleccionar Imagen", command=on_select_image)
select_image_button.pack(pady=10)

logout_label = Label(root, text="Presione Alt + F1 para desloguearse")  
logout_label.pack(pady=10)

atajo_teclado = {keyboard.Key.alt, keyboard.Key.f1}
teclas_presionadas = set()

def on_press(key):
    if any([key == k for k in atajo_teclado]):
        teclas_presionadas.add(key)

        if all([k in teclas_presionadas for k in atajo_teclado]):
            click_successful = click_on_button(button_image_path=ruta_del_boton)
            if not click_successful:
                # Utiliza after para llamar a set_not_found_label en el hilo principal después de un tiempo
                root.after(1, set_not_found_label, "¡Botón no encontrado!")
    else:
        teclas_presionadas.clear()

def on_release(key):
    if any([key == k for k in atajo_teclado]):
        teclas_presionadas.remove(key)

def on_exit():
    root.quit()  # Cierra la aplicación correctamente
    listener.stop()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Oculta la ventana en lugar de minimizarla
    root.withdraw()

    app_tray = AppTray(on_select_image, on_exit)
    app_tray.run_tray()

    root.mainloop()

    listener.join()