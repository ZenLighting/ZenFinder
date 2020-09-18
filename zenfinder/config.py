from dotenv import load_dotenv
load_dotenv()
import yaml
import os

mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")