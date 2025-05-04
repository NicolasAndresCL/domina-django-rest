# Domina Python: Django REST

Este es el repositorio del curso de LinkedIn Learning `Domina Python: Django REST`. El curso completo está disponible en [LinkedIn Learning][lil-course-url].

![Domina Python: Django REST][lil-thumbnail-url] 

Consulta el archivo Readme en la rama main para obtener instrucciones e información actualizadas.

Aprende a crear API REST eficientes utilizando Django REST Framework (DRF), el framework más potente para el desarrollo backend en Python. Este curso te guía paso a paso en la creación de una API REST, mostrando cómo integrar y aprovechar al máximo las funcionalidades de Django y DRF. Ideal para desarrolladores que desean mejorar sus habilidades en la creación de servicios web escalables, descubrirás cómo manejar solicitudes HTTP, autenticación, serialización de datos y más, todo dentro de un entorno flexible y robusto.

## Instrucciones
Este repositorio tiene un directorio con el nombre `movies_api`, donde encontrarás los archivos del proyecto de Django REST: los archivos de configuración y las aplicaciones. Por fuera del directorio del proyecto está el archivo `requirements.txt` con las dependencias requeridas para el correcto funcionamiento del proyecto.

## Instalación

1. Para utilizar estos archivos de ejercicios, debes tener descargado lo siguiente:
   - Python 3.11
   - Editor de código como VS Code o PyCharm
   - Conda o miniconda para el manejo de ambientes virtuales
2. Clona este repositorio en tu máquina local usando la Terminal (macOS), CMD (Windows), o una herramienta GUI como SourceTree.
3. Crea un ambiente virtual de Python con conda:

		conda create -n <nombre_ambiente> python=3.11

4. Activa el entorno:

		conda activate <nombre_ambiente>

5. Instala las librerías requeridas:

		pip install -r requirements.txt

6. Ingresa al directorio del proyecto:

		cd movies_api

7. Crea las migraciones:

		python manage.py makemigrations

8. Aplica las migraciones:

		python manage.py migrate

9. Crea un superusuario para acceder al panel de administración:

		python manage.py createsuperuser

10. Corre el proyecto:

		python manage.py runserver

11. **Nota importante:** si accedes a `http://127.0.0.1:8000/` y ves un error 404, se ha añadido una redirección automática a la documentación Swagger. Para esto se agregó lo siguiente en `movies_api/urls.py`:

```python
from django.shortcuts import redirect

def redirect_to_swagger(request):
    return redirect('/swagger/')

path("", redirect_to_swagger),


### Autor / Contribuciones

Este repositorio fue modificado por **Nicolás Cano** como parte de su proceso de aprendizaje en Django REST Framework.  
El proyecto original forma parte del curso de **Ana María Pinto** en [LinkedIn Learning](https://www.linkedin.com/learning/domina-python-django-rest).

Cambios realizados:

- Corrección de error 404 inicial con redirección automática a la documentación Swagger.
- Estructuración del entorno con conda.
- Organización del proyecto para futuras ampliaciones o prácticas personales.
