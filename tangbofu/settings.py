import os
from tangbofu.secret import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = SECRET['SECRET_KEY']
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'ckeditor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tangbofu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tangbofu.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tangbofu',
        'USER': 'tangbofu',
        'PASSWORD': SECRET['DB_PASSWORD'],
        'HOST': 'localhost'
    },
}

# Internationalization
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-CN'
DEFAULT_CHARSET = 'utf-8'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR + '/main/static'
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = BASE_DIR + '/main/data'
MEDIA_URL = '/data/'

# Email
EMAIL_HOST_USER = '59889869@qq.com' # cooll_websys2015@qq.com
EMAIL_HOST_PASSWORD = SECRET['EMAIL_HOST_PASSWORD']
EMAIL_HOST = 'smtp.qq.com' #'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Qiniu
QINIU_AK = SECRET['QINIU_AK']
QINIU_SK = SECRET['QINIU_SK']
QINIU_BUCKET_NAME = 'lnhote'
# Ckeditor
CKEDITOR_JQUERY_URL = STATIC_ROOT + '/main/js/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'ckeditor/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'CustomX',
        'toolbar_CustomX': [
            ['Bold', 'Italic', 'Underline', 'Font', 'FontSize', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image', 'Table', 'HorizontalRule', 'Smiley'],
            ['RemoveFormat'],
        ]
    }
}