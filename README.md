# Evaluación Sumativa N° 01 - Programación Back End

**Alumno:** Omar Barriga

Proyecto Django con dos aplicaciones (`app_uno` y `app_dos`), cada una con dos vistas independientes accesibles en el navegador.

## Estructura

| Rama              | Descripción                                                    |
| ----------------- | -------------------------------------------------------------- |
| `main`            | Integración final de ambas aplicaciones                        |
| `barrigaomarrama1`| App `app_uno` con dos vistas HTML                              |
| `barrigaomarrama2`| App `app_dos` con dos vistas HTML                              |

## Puesta en marcha

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py runserver
```

## Rutas disponibles

- `http://127.0.0.1:8000/` - Inicio (app_uno)
- `http://127.0.0.1:8000/uno/` - Vista 1 de app_uno
- `http://127.0.0.1:8000/uno/saludo/` - Vista 2 de app_uno
- `http://127.0.0.1:8000/dos/` - Vista 1 de app_dos
- `http://127.0.0.1:8000/dos/horario/` - Vista 2 de app_dos