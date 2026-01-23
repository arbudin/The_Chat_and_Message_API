import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#load_dotenv()

RUNNING_IN_DOCKER = os.getenv("RUNNING_IN_DOCKER", "false").lower() == "true"

# Загружаем нужный .env
if RUNNING_IN_DOCKER:
    load_dotenv(".env.docker")
else:
    load_dotenv(".env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# ссылка на БД
#DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

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

