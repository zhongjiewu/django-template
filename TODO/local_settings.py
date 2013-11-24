import os
from settings import PROJECT_ROOT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT,'dev.db'),
    }
}

