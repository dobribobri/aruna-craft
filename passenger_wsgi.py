# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0622997/data/www/aruna-craft.com/arunacraft')
sys.path.insert(1, '/var/www/u0622997/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'arunacraft.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()