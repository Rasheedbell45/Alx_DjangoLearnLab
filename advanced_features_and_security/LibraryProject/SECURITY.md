# Security Measures in LibraryProject

## Settings
- `DEBUG = False`: Prevents sensitive data leaks.
- `SECURE_BROWSER_XSS_FILTER = True`: Stops reflected XSS.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME sniffing.
- `X_FRAME_OPTIONS = "DENY"`: Stops clickjacking.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE = True`: Enforces HTTPS-only cookies.
- HSTS enabled to force HTTPS across all requests.
- Content Security Policy applied via `django-csp`.

## Templates
- All forms include `{% csrf_token %}`.

## Views
- All DB queries use Django ORM.
- Input validation handled with Django `forms.py`.

## Testing
- Tested CSRF by submitting forms without tokens → correctly blocked.
- Verified SQL injection attempts → safely escaped.
- CSP verified using browser DevTools (headers present).
