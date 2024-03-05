import os
import sys
import winreg as reg

def add_to_startup():
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    value_name = "Auto Deslogeo"  # Puedes cambiar esto al nombre de tu aplicación

    # Obtiene la ruta del ejecutable actual
    exe_path = os.path.abspath(sys.argv[0])

    try:
        # Abre la clave del Registro
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)

        # Agrega la entrada al Registro
        reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, exe_path)

        # Cierra la clave del Registro
        reg.CloseKey(reg_key)

        print(f'Se agregó "{value_name}" al inicio del sistema.')
    except Exception as e:
        print(f'Error al agregar al inicio del sistema: {e}')

def is_app_in_startup():
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    value_name = "Auto Deslogeo"  # Asegúrate de que coincida con el nombre que usas en add_to_startup

    try:
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_READ)
        value, _ = reg.QueryValueEx(reg_key, value_name)
        reg.CloseKey(reg_key)
        return value == os.path.abspath(sys.argv[0])
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f'Error al leer el Registro: {e}')
        return False