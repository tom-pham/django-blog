import os
import dj_database_url

from .settings import *

DATABASES = {"default": dj_database_url.config(default="sqlite://localhost")}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = ["*"]

MIDDLEWARE = {"whitenoise.middleware.WhiteNoiseMiddleware", *MIDDLEWARE}
