# Auth_ms

## Tabla de contenido

1. [Descripción](#descripción)
2. [Tecnología](#tecnología)
3. [Instalación](#instalación)

## Descripción

El objetivo de este **microservicio** es la administración de los usuarios. Al ser orquestado con una API Gateway permitirá la validación de cada permiso necesario para la utilización de otros microservicios.

---

## Tecnología

- Python version >= 3 (https://www.python.org/downloads/)
- Django
- Docker

---

## Instalación

Para su uso se debe implementar un archivo que contenga la clave secreta y la conexión a la base de datos. (En el presente proyecto se usó Postgres SQL)

- Crear archivo **sensitive.py** en _authMsProject/_ e incluir el siguiente código:

(Implementar una llave secreta propia)
`SECRET_KEY = ''`

(Incluir las credenciales propias de la BD)

```
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': '',
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}
```

- Crear carpeta env
  `$ python -m venv env` en consola command Prompt

- Activar un entorno
  `$ env\Scripts\activate` en consola command Prompt

- Instalar las librerías
  `$ pip install -r requirements.txt` en cualquier consola con (env) activado

- Ejecutar las migraciones
  **Peligro: Esto modifica la base de datos y crea un nuevo esquema, puede generar pérdida de información en caso de que la BD ya tenga un esquema**
  **No ejecutar este comando si la base de datos ya está en funcionamiento, a menos de que esta se desee modificar**
  `$ python manage.py migrate`

- Correr la aplicación
  `$ python manage.py runserver`

---
