from .base import *
import environ

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")
#"django-insecure-z8hfru31ySM5IB_3qV_AKOIkXL3mVU2qdMUEW09HEwnPM8D5u0KvJ5De2e586CIJZt8"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":env.str("DB_NAME"),
        "USER":env.str("DB_USER"),
        "PASSWORD":env.str("DB_PWD"),
        "HOST":env.str("DB_HOST"),
        "PORT":env.int("DB_PORT")
    }
}



