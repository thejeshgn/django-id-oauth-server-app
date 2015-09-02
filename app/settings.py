import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print "BASE_DIR="+str(BASE_DIR)

PROJECT_ROOT = os.path.dirname(__file__)
print "PROJECT_ROOT="+str(PROJECT_ROOT)

sys.path.insert(0,PROJECT_ROOT)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dr.sqlite3',
    },
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static/")
print "STATIC_ROOT="+str(STATIC_ROOT)
STATIC_URL ="/static/"


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'oauth2_provider',
    'corsheaders',
    'registration',

    'app',
)


ALLOWED_HOSTS = ['*']

SITE_ID = 1

ROOT_URLCONF = 'app.urls_default'

# TEMPLATE_LOADERS = (
#     'django.template.loaders.app_directories.Loader',
# )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)



AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)



try:
    print "TRYING TO IMPORT PRODUCTION SETTINGS"
    from production_settings import *
except ImportError:
    #If production settings are present don't import local settings
    print ">>>>> ERROR: NO PRODUCTION SETTINGS, ie. production_settings.py"
    try:       
        from local_settings import *
        print "USING TEST SETTINGS"
    except ImportError:
        pass
