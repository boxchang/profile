from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a$%ooy83#540*_u!$5sq7$q$(2414v=k7qrua7(d8nyk4qrith'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}