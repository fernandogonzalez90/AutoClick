# Auto Deslogeo

Este programa automatiza la acción de hacer clic en un botón específico en la pantalla cuando se presiona un atajo de teclado. Además, la versión principal incluye una interfaz gráfica (GUI) con un sistema de bandeja de notificaciones.
App Principal (Interfaz Gráfica y Sistema de Bandeja de Notificaciones)
### Dependencias

    pyautogui: Utilizado para realizar acciones de automatización, como hacer clic en la pantalla.
    time: Para introducir pausas entre acciones.
    pynput: Usado para detectar eventos de teclado.
    tkinter: Biblioteca de interfaz gráfica.
    pystray: Para gestionar el ícono en la bandeja de notificaciones.
    PIL: Se utiliza para cargar la imagen del ícono.

### Funcionamiento

    Selección de Imagen del Botón: El usuario puede seleccionar una imagen que represente el botón a hacer clic en la pantalla. Esta imagen se utiliza como referencia para la automatización.

    Atajo de Teclado: Se establece un atajo de teclado (Alt + F1 por defecto) para activar la acción de clic en el botón.

    Sistema de Bandeja de Notificaciones: El programa se ejecuta en segundo plano y se muestra como un ícono en la bandeja de notificaciones. Desde la bandeja, el usuario puede cargar una nueva imagen o salir de la aplicación.

    Automatización de Clic: Cuando se presiona el atajo de teclado, el programa busca la imagen del botón en la pantalla y realiza un clic si se encuentra.

#### Uso

    Ejecutar el programa, seleccionar la imagen del botón y minimizar la ventana.
    Presionar el atajo de teclado definido para hacer clic en el botón.

### Inicio Automático del Sistema

    La aplicación puede registrarse para iniciarse automáticamente con el sistema operativo.

### Módulo (reg.py)

Este módulo proporciona funciones para agregar la aplicación al inicio del sistema y verificar si ya está registrada.
Funciones

    add_to_startup()
        Agrega la aplicación al registro de inicio del sistema operativo.
    is_app_in_startup()
        Verifica si la aplicación ya está registrada para iniciar con el sistema.

#### Uso

    El módulo es utilizado en la app principal para gestionar el inicio automático.

### Versión CLI (Línea de Comandos)

Se proporciona una versión de línea de comandos que encapsula la lógica principal del programa.
Funcionamiento

    Se selecciona la imagen del botón mediante la línea de comandos.
    Se establece un atajo de teclado (Shift por defecto) para activar la acción de clic en el botón.
    Se imprime en la consola la información de la imagen seleccionada y se espera a que se presione el atajo de teclado.

#### Uso

bash

python cli_version.py img/boton.png

Nota: Asegúrate de tener todas las dependencias instaladas antes de ejecutar el programa.

Este README proporciona una visión general del funcionamiento del programa y su módulo asociado. Consulta el código fuente para obtener detalles específicos sobre implementaciones y configuraciones.