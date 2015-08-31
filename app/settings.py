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
    'django.contrib.admin',
    'oauth2_provider',
    'corsheaders',
    'registration',

    'app',
)

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = '_'

SITE_ID = 1

ROOT_URLCONF = 'app.urls_default'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)

#SMTP SETTINGS
EMAIL_HOST =''
EMAIL_PORT =''
EMAIL_HOST_USER='' 
EMAIL_HOST_PASSWORD='' 


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Your App Name]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
)