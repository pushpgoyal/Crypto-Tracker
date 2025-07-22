import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # Load variables from .env file

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

