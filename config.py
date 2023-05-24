import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5859491010:AAHdjkcotSxo2CglZ-c_jD5uk_uMOsvBgAo")
    
    API_ID = int(os.environ.get("API_ID", 26607105))
    
    API_HASH = os.environ.get("API_HASH", "ca6186c6553ffe7db21f8f0b67765337" )
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1287792972"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://umar786:umar786@cluster0.rpuio0h.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
