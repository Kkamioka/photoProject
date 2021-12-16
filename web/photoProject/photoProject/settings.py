"""
Django settings for photoProject project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ta&=su1x9=(7yb8@)ed2=3x&@jopl=lmk-(3@7jmjic=^@0#m5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # photoアプリを追加する
    'photo.apps.PhotoConfig',
    # accountsアプリを追加する
    'accounts.apps.AccountsConfig',
    # django-cleanupを追加する
     'django_cleanup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'photoProject.urls'

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

WSGI_APPLICATION = 'photoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Django3.2未満でプロジェクトを作成した場合は警告表示対策として以下の記述が必要
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# 使用言語を日本語に設定
LANGUAGE_CODE = 'ja'

# タイムゾーンを設定
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# staticフォルダーのフルパスを設定
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Userモデルの代わりにCustomUserモデルを使用する
AUTH_USER_MODEL = 'accounts.CustomUser'

# ログインページのURL
# 「ログイン中しか見られないページ」に「未ログインの状態」で
# アクセスした場合、LOGIN_URLのページにリダイレクトされる
LOGIN_URL = 'accounts:login'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# メール送信のためのクラスを設定
# ターミナルで確認する場合は以下のコメントアウトを解除してください
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# メールサーバーへの接続設定
# Gmailのアドレス、Gmailのアプリ用パスワードは
# お使いのものを入力してください
DEFAULT_FROM_EMAIL = 'xxxxxx@gmail.com'  # メールの送信元のアドレスを入力
EMAIL_HOST = 'smtp.gmail.com'            # GmailのSMPTサーバー　　　
EMAIL_PORT = 587                         # SMPTサーバーのポート番号
EMAIL_HOST_USER = 'xxxxxx@gmail.com'     # Gmailのアドレスを入力
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxx' # Gmailのアプリ用パスワードを入力
EMAIL_USE_TLS = True # SMTP サーバと通信する際に TLS (セキュア) 接続を使う

# mediaフォルダーの場所(BASE_DIR以下のmedia)を登録
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# mediaのURLを登録
MEDIA_URL = '/media/'
