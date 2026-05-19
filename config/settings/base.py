"""Shared Django settings for the project."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from django.contrib.messages import constants as messages
from django.core.exceptions import ImproperlyConfigured


BASE_DIR = Path(__file__).resolve().parents[2]


def load_dotenv(path: Path = BASE_DIR / ".env") -> None:
    """Load simple KEY=value pairs from .env without overriding real env vars."""

    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def env(key: str, default: Any = None, *, required: bool = False) -> Any:
    value = os.environ.get(key)
    if value in (None, ""):
        if required:
            raise ImproperlyConfigured(f"Missing required environment variable: {key}")
        return default
    return value


def env_bool(key: str, default: bool = False) -> bool:
    value = env(key, default=str(default))
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def env_list(key: str, default: str | list[str] = "", *, required: bool = False) -> list[str]:
    value = env(key, default=default, required=required)
    if isinstance(value, list):
        return value
    return [item.strip() for item in str(value).split(",") if item.strip()]


load_dotenv()


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-development-key-change-before-production",
)
DEBUG = env_bool("DJANGO_DEBUG", False)
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "core",
    "contacts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASE_ENGINE = str(env("DATABASE_ENGINE", "sqlite")).lower()

if DATABASE_ENGINE == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env("MYSQL_DATABASE", "portfolio_db"),
            "USER": env("MYSQL_USER", "root"),
            "PASSWORD": env("MYSQL_PASSWORD", ""),
            "HOST": env("MYSQL_HOST", "127.0.0.1"),
            "PORT": env("MYSQL_PORT", "3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / env("SQLITE_NAME", "db.sqlite3"),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = env("DJANGO_TIME_ZONE", "Asia/Kolkata")
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

MESSAGE_TAGS = {
    messages.DEBUG: "secondary",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "danger",
}

SITE_NAME = env("SITE_NAME", "Your Name")
SITE_TAGLINE = env("SITE_TAGLINE", "Full Stack Developer")
PORTFOLIO_INTRO = env(
    "PORTFOLIO_INTRO",
    "I design and build polished web products with clean interfaces, reliable backends, and thoughtful user experiences.",
)
PORTFOLIO_EMAIL = env("PORTFOLIO_EMAIL", "hello@example.com")
PORTFOLIO_PHONE = env("PORTFOLIO_PHONE", "+1 555 0100")
PORTFOLIO_LOCATION = env("PORTFOLIO_LOCATION", "Remote")
PORTFOLIO_GITHUB = env("PORTFOLIO_GITHUB", "https://github.com/")
PORTFOLIO_LINKEDIN = env("PORTFOLIO_LINKEDIN", "https://www.linkedin.com/")
PORTFOLIO_X = env("PORTFOLIO_X", "https://x.com/")
