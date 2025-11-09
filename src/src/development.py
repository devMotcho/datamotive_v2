import os

DEBUG = int(os.getenv("DEBUG", 0))
SECRET_KEY = str(os.getenv("SECRET_KEY", "unsafe-dev-secret"))
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


DATABASES = {
    "default": {
    "ENGINE": os.getenv("POSTGRES_ENGINE", "django.db.backends.postgresql"),
    "NAME": os.getenv("POSTGRES_DB", "database"),
    "USER": os.getenv("POSTGRES_USER", "user"),
    "PASSWORD": os.getenv("POSTGRES_PASSWORD", "password"),
    "HOST": os.getenv("POSTGRES_HOST", "db"),
    "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}