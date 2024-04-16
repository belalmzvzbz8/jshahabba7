import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6889060225:AAE9TbAD_iGu1tX9fSiCmLUBF1eb-E4tmNY", "")

    APP_ID = int(os.environ.get("APP_ID", 22865033))

    API_HASH = os.environ.get("API_HASH", "62ba116490803164ee88d4e477d5da84")
