import os

from dotenv import load_dotenv

load_dotenv()


def get_credentials():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    return {"username": username, "password": password}
