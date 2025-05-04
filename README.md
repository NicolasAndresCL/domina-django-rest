# Domina Python: Django REST		

Este es el repositorio del curso de LinkedIn Learning `Domina Python: Django REST`. El curso completo está disponible en [LinkedIn Learning][lil-course-url].

![Domina Python: Django REST][lil-thumbnail-url] 

Consulta el archivo Readme en la rama main para obtener instrucciones e información actualizadas.

Aprende a crear API REST eficientes utilizando Django REST Framework (DRF), el framework más potente para el desarrollo backend en Python. Este curso te guía paso a paso en la creación de una API REST, mostrando cómo integrar y aprovechar al máximo las funcionalidades de Django y DRF. Ideal para desarrolladores que desean mejorar sus habilidades en la creación de servicios web escalables, descubrirás cómo manejar solicitudes HTTP, autenticación, serialización de datos y más, todo dentro de un entorno flexible y robusto.

## Instrucciones
Este repositorio tiene un directorio con el nombre movies_api, donde encontrarás los archivos del proyecto de Django REST: los archivos de configuración y las aplicaciones. Por fuera del directorio del proyecto está el archivo `requirements.txt` con las dependencias requeridas para el correcto funcionamiento del proyecto.

## Instalación

1. Para utilizar estos archivos de ejercicios, debes tener descargado lo siguiente:
   - Python 3.11
   - Editor de código como VS Code o PyCharm
   - Conda o miniconda para el manejo de ambientes virtuales
2. Clona este repositorio en tu máquina local usando la Terminal (macOS) o CMD (Windows), o una herramienta GUI como SourceTree.
3. Crea un ambiente virtual de Python, puedes hacerlo con conda

		conda install -n <nombre_ambiente> python=3.11

4. Instala las librerías

		pip install -r requirements.txt

5. Ingresa al directorio del proyecto

		cd movies_api

6. Crea las migraciones

		python manage.py makemigrations

7. Aplica las migraciones

		python manage.py migrate

8. Crea un super usuario para el administrador

		python manage.py createsuperuser

9. Corre el proyecto

		python manage.py runserver

### Docente

**Ana María Pinto**

Echa un vistazo a mis otros cursos en [LinkedIn Learning](https://www.linkedin.com/learning/instructors/ana-maria-pinto).

[0]: # (Replace these placeholder URLs with actual course URLs)
[lil-course-url]: https://www.linkedin.com/learning/domina-python-django-rest
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQFhdVexFN6c_g/learning-public-crop_675_1200/B4EZWtZQQwG0Ac-/0/1742370834290?e=2147483647&v=beta&t=fYFlrJ4Nx5x7mf_vyThE68pRx1XbtPqJKAyag6qxpwo

[1]: # (End of ES-Instruction ###############################################################################################)
