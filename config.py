import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youwill-never-guess-canitbeshown'  # can it be shown openly?
