import os

API_ID    = os.environ.get("API_ID", "26993113")
API_HASH  = os.environ.get("API_HASH", "bea8bb154b07fc50ee3e308772f4366c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7221435726:AAE36beQ0pqDrdfHb03i63BXdkvbm5HGuic") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
