from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import app
from django.utils import html
import os
from colorama import Fore
import docker
import re
import subprocess
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlateformeAntivirale.settings')

app = Celery('PlateformeAntivirale', broker='amqp://guest@localhost//', backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()