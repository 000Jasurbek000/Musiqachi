"""
ASGI config for education_portal project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_portal.settings')

application = get_asgi_application()
