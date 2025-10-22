import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "timmy-secret")
    APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")  # used for CSS cache-bust
