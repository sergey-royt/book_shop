from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from models import Base


load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def main() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
