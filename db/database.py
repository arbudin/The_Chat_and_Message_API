from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user = 'postgres'
db_password = ''
db_host = 'localhost'
db_port = '5432'
db_name = 'chats_and_messages_db'

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

