import os

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test_settings')

