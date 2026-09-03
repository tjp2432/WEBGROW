import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def _database_uri():
    uri = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "perrones.db")}')
    if uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    return uri


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'perrones-inc-secret-key-2026')
    FORCE_HTTPS = os.environ.get('FORCE_HTTPS', '0') == '1'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = FORCE_HTTPS
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = FORCE_HTTPS
    SQLALCHEMY_DATABASE_URI = _database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'images')
    PER_PAGE = 12
