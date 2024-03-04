import pyautogui
import time
from threading import Thread
import tkinter as tk
from tkinter import filedialog

from pynput import keyboard
from pynput.keyboard import Key, KeyModifier
from pynput.keyboard._base import KeyCode


class Configurator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Configurador de Botón")
        self.geometry("400x400")

        self.button_image_path = None
        self.hotkey_combination = "alt+f1"
        self.save_status = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label y botón para seleccionar imagen
        self.image_path_label = tk.Label(self, text="Ruta de la imagen del botón:")
        self.image_path_label.pack(pady=10)
        self.select_image_button = tk.Button(self, text="Seleccionar Imagen", command=self.select_image)
        self.select_image_button.pack()

        # Label y botón para detectar teclas
        self.hotkey_label = tk.Label(self, text="Combinación de teclas:")
        self.hotkey_label.pack(pady=10)
        self.detect_hotkey_button = tk.Button(self, text="Detectar Teclas", command=self.detect_hotkey)
        self.detect_hotkey_button.pack()

        # Label y botón para guardar configuración
        self.save_status_label = tk.Label(self, textvariable=self.save_status)
        self.save_status_label.pack(pady=10)
        self.save_configuration_button = tk.Button(self, text="Guardar Configuración", command=self.save_configuration)
        self.save_configuration_button.pack(pady=20)

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Seleccionar Imagen",
                                               filetypes=[("Image files", (".png", ".jpg", ".jpeg"))])
        if file_path:
            self.button_image_path = file_path
            self.image_path_label.config(text=f"Ruta de la imagen del botón: {file_path}")

    def save_configuration(self):
        if self.button_image_path is not None and self.hotkey_combination is not None:
            self.save_status.set("Guardado correctamente")
            print(f"Ruta de la imagen: {self.button_image_path}")
            print(f"Combinación de teclas: {self.hotkey_combination}")
        else:
            self.save_status.set("Error al guardar configuración")

    def detect_hotkey(self):
        # Deshabilita el botón mientras se detecta la combinación de teclas
        self.detect_hotkey_button.config(state=tk.DISABLED)

        print("Presiona la combinación de teclas...")

        # Crea un listener para capturar las pulsaciones de teclas
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()

        # Convierte la tecla presionada en una cadena
        hotkey_str = str(hotkey)

        # Actualiza el label con la nueva combinación
        self.hotkey_label.config(text=f"Combinación de teclas: {hotkey_str}")

        # Habilita el botón nuevamente
        self.detect_hotkey_button.config(state=tk.NORMAL)

    def _on_press(self, key):
        global hotkey

        # Si se presiona la tecla Escape, cancela la detección
        if key == Key.esc:
            return False

        # Si se presiona una tecla modificadora, guarda su nombre
        elif isinstance(key, KeyModifier):
            modifier_name = KeyCode(key).name
            if modifier_name not in self.hotkey_combination:
                self.hotkey_combination.append(modifier_name)

        # Si se presiona una tecla normal, guarda su nombre y finaliza la detección
        else:
            hotkey = key
            self.detect_hotkey_button.invoke()


if __name__ == "__main__":
    configurator = Configurator()
    configurator.protocol("WM_DELETE_WINDOW", configurator.destroy)  # Cierra la ventana principal correctamente
    configurator.mainloop()
