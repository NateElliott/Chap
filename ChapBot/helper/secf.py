from django.conf import settings
import os

def load(name):

    file = '{}.txt'.format(name)

    with open(os.path.join(settings.SEC_DIR, file), 'rb') as f:
        data = f.read().decode('utf-8', 'ignore')
    f.close()

    return data
