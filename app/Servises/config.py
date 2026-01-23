from dotenv import load_dotenv
from pathlib import Path
import os

current_dir = Path(__file__).parent

dotenv_path = current_dir.parent / ".." / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path)
else:
    print(f".env is no exist at {dotenv_path}")


secret_key = os.getenv("SECRET_KEY")
algoritm = os.getenv("ALGORITM")
key_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")