# Polotic-Python-Django
🐍 Repositorio para subir prácticas hechas en cada clase

[Ver lista de clases (main)](https://github.com/JaviCeRodriguez/Polotic-Python-Django/tree/main) | Clase 02 ⏭

## Clase 01
Teoría: [Diapositivas de Clase 01]()

## Ejercicios
1) **Comencemos instalando Python en nuestra computadora y probando mediante `python --version` si lo hemos hecho bien.**
- Instalamos Python [página oficial](https://www.python.org/).
- Abrimos la consola desde:
    - Inicio > tipeamos cmd > Enter
    - o Win + R > tipeamos cmd > Enter
    - Tipeamos `python --version`


2) **Intentemos instalar nuestras propias entidades virtuales y dialoguemos sobre como nos fue.**
- Instalamos virtualenv desde consola: `pip install virtualenv`
- Iniciamos proyecto nuevo (por lo general le ponemos de nombre "venv"): `virtualenv -p python3 venv
- Activamos el entorno creado: `venv\Scripts\activate`
- Instalamos paquetes como siempre: `pip install requests`
- Ejecutamos el archivo principal: `python main.py`
- Guardamos en un texto las dependencias: `python -m pip freeze > requirements.txt`
- Si ya lo tenemos creado y no tenemos instalada alguna dependencia: `python -m pip install -r requirements.txt`
- Desactivamos entorno: `deactivate`