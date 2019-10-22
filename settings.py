import os

PROJECT_ID = os.environ.get('PROJECT_ID')
TRIGGERS_FILTER_REGEX = os.environ.get('TRIGGERS_FILTER_REGEX', '^.*$')
