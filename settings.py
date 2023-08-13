from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR.joinpath('.env')
if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)
