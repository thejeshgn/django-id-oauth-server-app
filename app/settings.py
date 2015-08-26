DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dr.sqlite3',
    },
}

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