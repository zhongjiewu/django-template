from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raas.settings')

app = Celery('raas',
             include=['raas.tasks'])
app.config_from_object('django.conf:settings')
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)
#app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
