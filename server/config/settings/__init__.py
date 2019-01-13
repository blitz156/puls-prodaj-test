from os.path import dirname

ROOT_PATH = dirname(dirname(dirname(__file__)))

from .installed_apps import *
from .settings import *

ALLOWED_HOSTS = ['*']

try:
    from local import *
except ImportError:
    pass
