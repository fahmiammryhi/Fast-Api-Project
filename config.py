# config.py
from dotenv import load_dotenv
import os

load_dotenv()

FLIP_SECRET = os.getenv("FLIP_SECRET")
