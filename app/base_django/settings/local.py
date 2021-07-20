from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']  # 모든 호스트 허용

WSGI_APPLICATION = 'base_django.wsgi.local.application'  # 수정

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ["127.0.0.1"]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
