import os
import json
from dotenv import load_dotenv, dotenv_values
from .fetch import fetch_env

def load(is_init=False, cache_enabled=None, dot_env_enabled=True, dot_env_path=".env"):
  if is_init and os.environ.get("ENVKEY_DISABLE_AUTOLOAD"):
    return dict()

  if is_init and dot_env_enabled:
    if dotenv_values(dot_env_path).get("ENVKEY_DISABLE_AUTOLOAD"):
      return dict()

  if dot_env_enabled:
    dot_env_res = load_dotenv(os.path.join(os.getcwd(), dot_env_path))

    if cache_enabled == None:
      cache_enabled = dot_env_res == True

  key = os.environ.get("ENVKEY")

  if key == None:
    raise ValueError("ENVKEY missing - must be set as an environment variable or in a gitignored .env file in the root of your project. Go to https://www.envkey.com if you don't know what an ENVKEY is.")

  fetch_res = fetch_env(key, cache_enabled=cache_enabled)

  vars_set = dict()

  for k in fetch_res:
    if os.environ.get(k) == None:
      os.environ[k] = fetch_res[k]
      vars_set[k] = fetch_res[k]

  return vars_set