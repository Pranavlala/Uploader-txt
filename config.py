# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "10583548"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "c6825265a7ad87f7537c0b52f8b74a43")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7276120323:AAH9aF0clIc1LUZUW_i-8I6s61ah-69kT0c")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Merakhudkaextractorbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7410986089"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7410986089").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srvter")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-100"))

