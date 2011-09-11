# -*- coding: utf-8 -*-
'''

@author: Niko Skrypnik
Created: 6-09-2011
filedescr: Example of sushi launch file

'''

import os
os.environ['SUSHI_SETTINGS_MODULE'] = 'settings'

from sushi.core import run_server

run_server('127.0.0.1')
