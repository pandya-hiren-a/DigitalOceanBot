from config import get_env


class EnvConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = get_env('SECRET')


class DevelopmentEnv(EnvConfig):
    DEBUG = True


class TestingEnv(EnvConfig):
    TESTING = True
    DEBUG = True


class StagingEnv(EnvConfig):
    DEBUG = True


class ProductionEnv(EnvConfig):
    DEBUG = False
    TESTING = False


app_env = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'staging': StagingEnv,
    'production': ProductionEnv
}
