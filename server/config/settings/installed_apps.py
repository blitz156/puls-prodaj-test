INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django_redis',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
)

LOCAL_APPS = (
    'apps.puls_prodaj_test',
)

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {
    app_name: MIGRATION_PATH + app_name
    for app_name in LOCAL_MIGRATIONS
}
