# -*- coding: utf-8 -*-
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u1793832/data/www/kudrinofficial.ru/')
sys.path.insert(1, '/var/www/u1793832/data/venv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

application = get_wsgi_application()
