from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']  # 모든 호스트 허용

WSGI_APPLICATION = 'base_django.wsgi.dev.application'  # 수정

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

