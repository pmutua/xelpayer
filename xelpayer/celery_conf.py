# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','xelpayer.settings')
app = Celery('xelpayer')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)