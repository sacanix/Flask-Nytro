import os

DEBUG = True

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % os.path.join(APP_ROOT, 'database.db')
SQLALCHEMY_ECHO = True

SECRET_KEY = 'ZXZe7PVri+-bK-4UYE1VtbI#JS@l7yGT0z)JIqnW2#d6DQK=dvhRN0_lyVegLahqM@7Ij3wDlTb5t@Z0CeudU=TOP5Ss-twoNVrEG+QKFF92wlnm2JZs$2U6yx3$e@PC'

BLUEPRINTS = (
    'sample_app.site',
)