import os
import urllib
from pathlib import Path
import urllib.parse

from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]
X_FRAME_OPTIONS = "SAMEORIGIN"
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True

CLOUDRUN_SERVICE_URL = os.environ.get("CLOUDRUN_SERVICE_URL")
if CLOUDRUN_SERVICE_URL:
    # DEBUG = False
    ALLOWED_HOSTS = [urllib.parse.urlparse(CLOUDRUN_SERVICE_URL).netloc]
    CORS_ALLOWED_ORIGINS = [CLOUDRUN_SERVICE_URL]
    CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL]
else:
    from dotenv import load_dotenv

    # load .env file
    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    LOCAL_DOMAIN = os.environ.get("LOCAL_DOMAIN")
    if LOCAL_DOMAIN:
        ALLOWED_HOSTS = [urllib.parse.urlparse(LOCAL_DOMAIN).netloc]
        CORS_ALLOWED_ORIGINS = [LOCAL_DOMAIN]
        CSRF_TRUSTED_ORIGINS = [LOCAL_DOMAIN]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# Application definition

INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "markdownx",
    "emoji",
    "mdeditor",
    "colorfield",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "personal_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "personal_blog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DATABASE"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "ja"
if not LANGUAGE_CODE:
    raise ValueError("LANGUAGE_CODE is not set.")

# TIME_ZONE = "UTC"
TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "media/"

if os.environ.get("STATIC_HOST"):
    gs_secret_file_path = os.environ.get("GS_SECRET_KEY_PATH")
    if not gs_secret_file_path:
        raise ValueError("GS_SECRET_KEY_PATH is not set.")

    if os.environ.get("GS_DEFAULT_ACL"):
        GS_DEFAULT_ACL = os.environ.get("GS_DEFAULT_ACL")
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        os.path.join(BASE_DIR, gs_secret_file_path)
    )

    STATIC_URL = os.environ.get("STATIC_HOST")
    if not STATIC_URL:
        raise ValueError("STATIC_HOST is not set.")
    MEDIA_URL = STATIC_URL + "/media/"
    STORAGES = {
        "default": {"BACKEND": os.environ.get("DEFAULT_FILE_STORAGE")},
        "staticfiles": {"BACKEND": os.environ.get("STATICFILES_STORAGE")},
        "media": {"BACKEND": os.environ.get("STATICFILES_STORAGE")},
    }
    GS_BUCKET_NAME = os.environ.get("GS_BUCKET_NAME")

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",  # table、code block etc..
    "markdown.extensions.codehilite",  # sintax highlight
    "markdown.extensions.toc",  # table of contents
    "markdown.extensions.nl2br",  # new line to <br>
    "markdown.extensions.admonition",  # attention block
    "markdown.extensions.sane_lists",  # list
]

EMOJI_REPLACE_HTML_ENTITIES = True

# settings for mdedter
MDEDITOR_CONFIGS = {
    "default": {
        "language": (
            os.environ.get("MDEDITER_LANGUAGE_CODE")
            if os.environ.get("MDEDITER_LANGUAGE_CODE")
            else "en"
        ),
        "upload_image_url": "image/",
        "toolbar": [
            "undo",
            "redo",
            "|",
            "bold",
            "del",
            "italic",
            "quote",
            "ucwords",
            "uppercase",
            "lowercase",
            "|",
            "h1",
            "h2",
            "h3",
            "h5",
            "h6",
            "|",
            "list-ul",
            "list-ol",
            "hr",
            "|",
            "link",
            "reference-link",
            "code",
            "preformatted-text",
            "code-block",
            "table",
            "datetime",  # "image",
            "emoji",
            "html-entities",
            "pagebreak",
            "goto-line",
            # "|",
            # "help", "info",
            "||",
            "preview",
            "watch",
            "fullscreen",
        ],  # custom edit box toolbar
        "lineWrapping": True,
    }
}
