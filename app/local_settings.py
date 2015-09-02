from settings import *

#***************************CHANGE FOR PROD SETTINGS *******************************#
SECRET_KEY = '_'

DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dr.sqlite3',
    },
}

#SMTP SETTINGS
EMAIL_HOST ='smtp.sendgrid.net'
EMAIL_PORT ='587'
EMAIL_HOST_USER='' 
EMAIL_HOST_PASSWORD='' 
DEFAULT_FROM_EMAIL='noreply@yourdomain.com'

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Your App Name]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


#*************************** END CHANGE FOR PROD SETTINGS ******************************#
