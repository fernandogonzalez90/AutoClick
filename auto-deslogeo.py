import pyautogui
import time
from pynput import keyboard
from tkinter import Tk, filedialog, Button, Label

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

def on_select_image():
    global ruta_del_boton
    ruta_del_boton = select_image()

    # Actualizar la etiqueta con la nueva ruta
    message_label.config(text=f"Imagen seleccionada:\n{ruta_del_boton}")
    not_found_label.config(text="")  # Limpiar el mensaje de "no encontrado"

# Ruta inicial de la captura del botón
ruta_del_boton = 'img/boton.png'

# Crear la ventana principal
root = Tk()
root.title("Auto Deslogeo")  # Cambiar el título de la ventana
root.geometry("400x200")  # Cambiar el tamaño de la ventana a 400 píxeles de ancho y 300 píxeles de alto

# Crear etiquetas y un botón en la ventana principal
message_label = Label(root, text=f"Imagen seleccionada:\n{ruta_del_boton}")
message_label.pack(pady=10)

not_found_label = Label(root, text="")
not_found_label.pack(pady=10)

select_image_button = Button(root, text="Seleccionar Imagen", command=on_select_image)
select_image_button.pack(pady=10)

# Agregar el nuevo label indicando cómo desloguearse
logout_label = Label(root, text="Presione Alt + F1 para deslogearse")
logout_label.pack(pady=10)

# Definir el atajo de teclado (Alt + F1)
atajo_teclado = {keyboard.Key.alt, keyboard.Key.f1}

# Variables para rastrear el estado de las teclas
teclas_presionadas = set()

# Función que se ejecuta cuando se presiona una tecla
def on_press(key):
    if any([key == k for k in atajo_teclado]):
        teclas_presionadas.add(key)

        # Verificar si se presionaron todas las teclas del atajo
        if all([k in teclas_presionadas for k in atajo_teclado]):
            click_on_button(button_image_path=ruta_del_boton)
    else:
        teclas_presionadas.clear()

# Función que se ejecuta cuando se suelta una tecla
def on_release(key):
    if any([key == k for k in atajo_teclado]):
        teclas_presionadas.remove(key)

# Configurar y empezar a escuchar eventos de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Iniciar el bucle principal de tkinter
    root.mainloop()
    listener.join()
