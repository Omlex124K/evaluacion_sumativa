"""
Configuración de ASGI para el proyecto mi_proyecto.

Expone el objeto llamable de ASGI como variable de nivel de módulo ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')

application = get_asgi_application()
