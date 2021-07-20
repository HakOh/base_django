from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']  # 추후 배포할 호스트 주소 입력 예정

WSGI_APPLICATION = 'base_django.wsgi.prod.application'  # 수정

INSTALLED_APPS += []

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
