from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Applied AI Backend")
    ENV = os.getenv("ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()
