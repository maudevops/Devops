import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read environment variables
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "27017")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("MONGO_USERNAME")
DB_PASSWORD = os.getenv("MONGO_PASSWORD")

# Build MongoDB URI
if DB_USER and DB_PASSWORD:
    MONGO_URI = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin"
else:
    MONGO_URI = f"mongodb://{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Export the config as a dictionary
config = {
    "DB_NAME": DB_NAME,
    "DB_PORT": DB_PORT,
    "DB_HOST": DB_HOST,
    "MONGO_USERNAME": DB_USER,
    "MONGO_PASSWORD": DB_PASSWORD,
    "MONGO_URI": MONGO_URI
}

