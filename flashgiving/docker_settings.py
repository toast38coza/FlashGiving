## docker settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
ALLOWED_HOSTS = ['.flashgive.co.za', 'docker.local']
DEBUG = False
PAYFAST_URL = "https://www.payfast.co.za/eng/process"
