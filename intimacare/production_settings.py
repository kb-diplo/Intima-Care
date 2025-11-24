"""
Production settings for IntimaCare on PythonAnywhere
"""
from .settings import *
from decouple import config
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update allowed hosts for production
ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',  # Replace with your PythonAnywhere domain
    'intimacare.pythonanywhere.com',    # Example domain
    'localhost',
    '127.0.0.1',
]

# Database for production (you can use MySQL on PythonAnywhere)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'yourusername$intimacare',
#         'USER': 'yourusername',
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': 'yourusername.mysql.pythonanywhere-services.com',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# Static files configuration for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings (uncomment when using HTTPS)
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://yourusername.pythonanywhere.com",
    "https://intimacare.pythonanywhere.com",
]

# Email configuration for production (optional)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
