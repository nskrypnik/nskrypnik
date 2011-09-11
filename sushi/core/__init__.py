# -*- coding: utf-8 -*-

'''

@author: Niko Skrypnik
Created: 6-09-2011
filedescr: Core module of Sushi framework

'''
import os
from sushi.core.exceptions import DjangoImportError, SettingsError

# Base validation
try:
    import django
except ImportError as e:
    raise DjangoImportError('Importing of Django fault with "%s".\nIt seems that Django is not installed. Install Django first to run Sushi application.')

DJANGO_ENV_VARIABLE = "DJANGO_SETTINGS_MODULE"
SUSHI_ENV_VARIABLE = "SUSHI_SETTINGS_MODULE"

# Check the settings module

if not os.environ.get(DJANGO_ENV_VARIABLE):
    if os.environ.get(SUSHI_ENV_VARIABLE):
        os.environ[DJANGO_ENV_VARIABLE] = os.environ.get(SUSHI_ENV_VARIABLE)
    else:
        raise SettingsError('Settings environ variable is not set. Specify DJANGO_SETTINGS_MODULE or SUSHI_SETTINGS_MODULE environment variable')

from sushi.server import server
from sushi.core.application import Application


def run_server(HOST='', PORT=8080):
    " Starts sushi application with on HOST:PORT "    
    server.WebSocketServer((HOST, PORT), Application()).serve_forever()
