# Auth_ms

## Tabla de contenido

1. [Descripción](#Descripción)
2. [Tecnología](#Tecnología)
3. [Instalación](#instalación)

# Descripción

El objetivo de este microservicio es la administración de los usuarios. Al ser orquestado con una API Gateway permitirá la validación de cada permiso necesario para la utilización de otros microservicios.

---

# Tecnología

- Python >3 (https://www.python.org/downloads/)
- Django
- Docker

---

# Instalación

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
	'PORT': '', }
}
```

- en consola command Prompt:
  $ python -m venv env

- Activar un entorno en consola command Prompt:
  $ env\Scripts\activate

- Instalar las librerías:
  $ pip install -r requirements.txt

- Ejecutar las migraciones:
  $ python manage.py migrate

---
