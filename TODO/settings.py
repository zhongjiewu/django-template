###> insert in head
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

###> insert in middle
STATIC_ROOT = 'static'

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static-lib"),
)

# add this to STATICFILES_FINDERS
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
)

# add this to TEMPLATE_DIRS
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

# additional APPS
INSTALLED_APPS = (
    'south',
    'compressor',
)

# COMPRESSOR SETTINGS
# More info can be found at
# http://django-compressor.readthedocs.org/en/latest/settings/
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_OUTPUT_DIR = "cache"

# import local settings
try:
    from local_settings import *
except ImportError:
    pass
