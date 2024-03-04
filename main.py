import ctypes

# Definir la ruta al archivo .bat
ruta_bat = r"main.py"

# Crear una clave en el registro
key = ctypes.windll.regedit.OpenKey(
    ctypes.wintypes.HKEY_CURRENT_USER,
    r"Software\Microsoft\Windows\CurrentVersion\Run",
    0,
    ctypes.wintypes.KEY_WRITE
)

# Establecer el valor de la clave
ctypes.windll.regedit.SetStringValue(
    key,
    "Auto Deslogeo",
    ctypes.wintypes.REG_SZ,
    ruta_bat,
    len(ruta_bat) * 2
)

# Cerrar la clave
ctypes.windll.regedit.CloseKey(key)

# Reiniciar la computadora
ctypes.windll.user32.ExitWindowsEx(0, 0)
