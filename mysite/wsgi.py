"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


import os
import time
import traceback
import signal
import sys

#ServerAdmin webmaster@localhost
#
sys.path.append('/home/mingyu/PycharmProjects/OJ/misite')
sys.path.append('/home/mingyu/PycharmProjects/OJ')
sys.path.append('/home/mingyu/PycharmProjects/OJ/venv/lib/python3.6/site-packages')
sys.path.append('/home/mingyu/PycharmProjects/OJ/venv/lib/python3.6/site-packages/django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

try:
    application = get_wsgi_application()
except Exception:
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)