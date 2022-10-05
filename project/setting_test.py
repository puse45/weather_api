# Set a variable to show that we're in the testing enviroment
TESTING = True
from .settings import *  # noqa

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

DEBUG = False
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS += ("test_without_migrations",)  # noqa
