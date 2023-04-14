"""
ASGI config for company project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
# ASGI - Asynchronous Server Gateway Interface : Unordered Request and Response eg.Watsapp chat
import os 

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company.settings')

application = get_asgi_application()
