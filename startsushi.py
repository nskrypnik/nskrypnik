# -*- coding: utf-8 -*-
'''

@author: Niko Skrypnik
Created: 6-09-2011
filedescr: Example of sushi launch file

'''

import os
os.environ['SUSHI_SETTINGS_MODULE'] = 'settings'

from sushi.core import run_server
from sushi import settings

HOST = "0.0.0.0" # default localhost
PORT = "8080"

if hasattr(settings, 'SUSHI_HOST'):
    HOST = settings.SUSHI_HOST

if hasattr(settings, 'SUSHI_PORT'):
    PORT = settings.SUSHI_PORT

PORT = int(PORT)

run_server(HOST, PORT)
