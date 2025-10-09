INSTALLED_APPS = [
    # django default apps...
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third party
    "rest_framework",
    "rest_framework.authtoken",

    # your apps
    "accounts",
]

# custom user model
AUTH_USER_MODEL = "accounts.User"

# rest framework settings (simple example)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        # optionally add SessionAuthentication during dev:
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

# near bottom
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
