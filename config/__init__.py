from os import path, environ
from dotenv import load_dotenv

env_path = path.join(path.dirname(__file__), path.pardir, '.env')
load_dotenv(env_path, override=True)

''' User defined get_env function to get environment variables.
    Local uses .env file, while on the server such as heroku, we have to mention them in the config vars '''


def get_env(key):
    return environ.get(key)
