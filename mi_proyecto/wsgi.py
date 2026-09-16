"""
Configuración de WSGI para el proyecto mi_proyecto.

Expone el objeto llamable de WSGI como variable de nivel de módulo ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')

application = get_wsgi_application()
