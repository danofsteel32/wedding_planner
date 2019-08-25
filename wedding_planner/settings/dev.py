from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_db',
        'USER': 'dev',
        'PASSWORD': 'devpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
