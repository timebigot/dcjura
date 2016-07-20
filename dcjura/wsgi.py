"""
WSGI config for dcjura project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcjura.settings")

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
