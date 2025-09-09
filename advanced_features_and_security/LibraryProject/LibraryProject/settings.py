import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Ensure DEBUG is False in production
DEBUG = False

# Set your production host(s)
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com", "127.0.0.1"]

# --- Force HTTPS / HSTS ---
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",  # your custom app
]
INSTALLED_APPS += ["csp"]

MIDDLEWARE += [
    "csp.middleware.CSPMiddleware",
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

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "LibraryProject.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom User Model
AUTH_USER_MODEL = "bookshelf.CustomUser"

# Media settings (for profile photos)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# HTTP Strict Transport Security - instructs browsers to talk HTTPS only
# Use a low value for initial testing (e.g. 60), then increase to 31536000 (1 year)
SECURE_HSTS_SECONDS = 60               # <--- set to 60 for initial testing, then 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # include subdomains in HSTS policy
SECURE_HSTS_PRELOAD = False            # set True only after you register the domain for HSTS preload

# If behind a proxy/load balancer (like nginx), set this to recognize HTTPS
# Example: ('HTTP_X_FORWARDED_PROTO', 'https')
# Uncomment and configure if you proxy SSL at a front-end server:
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- Cookies ---
# Ensure cookies are only sent via HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent JavaScript from accessing session cookie where possible
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # CSRF cookie typically needs to be readable by JS if you do AJAX with CSRF header; keep default unless you change your approach

# Optionally limit cookie domain/path, e.g.:
# SESSION_COOKIE_DOMAIN = ".yourdomain.com"

# --- Browser protections ---
SECURE_CONTENT_TYPE_NOSNIFF = True   # Prevent content-type sniffing
SECURE_BROWSER_XSS_FILTER = True     # Enables the browser's XSS filtering
X_FRAME_OPTIONS = "DENY"             # Prevent site being framed (clickjacking protection)
# Alternatively X_FRAME_OPTIONS = "SAMEORIGIN" if you need frames from same origin.

# --- Content Security Policy (optional but recommended) ---
# If you use django-csp, configure it. Otherwise you can set CSP headers in middleware or at nginx.
# Example (using django-csp - install django-csp and add to INSTALLED_APPS and MIDDLEWARE)
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", "cdnjs.cloudflare.com")
# CSP_STYLE_SRC = ("'self'", "fonts.googleapis.com")
# CSP_IMG_SRC = ("'self'", "data:")

# --- Other hardening ---
# Prevent user enumeration via debug info - ensure DEBUG False
# Set secure session serializer and password hashers if needed (Django defaults are secure)
# PASSWORD_HASHERS = ['django.contrib.auth.hashers.Argon2PasswordHasher', ...]  # consider Argon2 in production

# --- Media/static hosting ---
# Static/media should be served by the web server (nginx, CDN). If serving with Django in dev, ensure DEBUG True only in dev.

# Logging for security events (optional)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}
