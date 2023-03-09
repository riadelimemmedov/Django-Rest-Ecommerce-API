from decouple import config

env = config('ENVIRONMENT',default='LOCAL')

if env == 'LOCAL':#development
    print('<You are in the LOCAL environment>')
    from .development import *
elif env == 'PROD':#production
    print('<Warning ! You are in the PROD environment>')
    from .production import *