import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "28200856")
    API_HASH = environ.get("API_HASH", "30e0567e3c97b0ea8e8d3fe50b2c2442")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8176591955:AAEMtVB2K3REPmX6gQh-soV5KWtHFJ0dTgk") 
    BOT_SESSION = environ.get("BOT_SESSION", "Fjejwjsk") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://nowkavya:SQhrAFthqs0mZLBT@cluster0.9e8dz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "nowkavya")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7154442141').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002390831521'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002352652410") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = [6071888646,7718610083]
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
