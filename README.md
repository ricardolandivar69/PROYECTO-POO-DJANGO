# Django Project Setup

Este archivo te guiará a través de los pasos necesarios para levantar un proyecto en Django utilizando un entorno virtual llamado `ent_virt`.

## Requisitos previos

- Python 3.8 o superior instalado en tu sistema.
- Pip, el gestor de paquetes de Python.

## Instrucciones

1. **Clona el repositorio (si es necesario)**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>

2. **Crea el entorno virtual `ent_virt`**

    ```bash
    python -m venv ent_virt

3. **Activa el entorno virtual**

    - En **Linux/macOS**:
        ```bash
        source ent_virt/bin/activate
    - En **Windows**:
        ```bash
        ent_virt\Scripts\activate
4. **Instala las dependencias del proyecto**
    ```bash
    pip install -r requirements.txt

5. **Ejecuta las migraciones**
    - Asegúrate de que la base de datos esté sincronizada ejecutando:
        ```bash
        python manage.py migrate
6. **Inicia el servidor de desarrollo**
    - Finalmente, levanta el servidor de Django:
        ```bash
        python manage.py runserver