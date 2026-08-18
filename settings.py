INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'channels',
    'core',
    'storages',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # React dev
    'https://yourdomain.com',
]

# Channels
ASGI_APPLICATION = 'kersa_backend.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {'hosts': [('127.0.0.1', 6379)]},
    },
}

# R2 Storage
AWS_ACCESS_KEY_ID = os.environ.get('R2_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('R2_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'your-bucket'
AWS_S3_ENDPOINT_URL = 'https://<accountid>.r2.cloudflarestorage.com'
AWS_S3_CUSTOM_DOMAIN = 'cdn.yourdomain.com'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'