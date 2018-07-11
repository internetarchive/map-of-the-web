"""
WSGI config for Query project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

import sys
from os.path import dirname, abspath
sys.path.append("./Query")
sys.path.append('/home/zcheng/foundationDB/Build/ENV/lib/python3.5/site-packages')


from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
  
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Query.settings")
os.environ["DJANGO_SETTINGS_MODULE"] =  "Query.settings"
application = get_wsgi_application()
