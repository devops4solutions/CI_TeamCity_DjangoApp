import os
from .base import *  # noqa

DEBUG = bool(os.environ.get('DJANGO_DEBUG', 'true'))

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
