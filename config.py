
import os

class Config:

    BOT_TOKEN = "8111089071:AAFO4wx2_jhq1ZQwXKf_OR4iNlcymxwAj20"
    APP_ID = 16016703
    API_HASH = "2e661b4ea5fa6d75640f12ea09f1c3a9"

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','5314733603,6022020248,5996829431,6136203777,7235663635').split(',')]

    DOWNLOAD_DIR = 'downloads'
