import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# ссылка на БД
DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# движок с ссылкой на БД
engine = create_engine(DATABASE_URL)

# фабрика сессий
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# получаем БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

