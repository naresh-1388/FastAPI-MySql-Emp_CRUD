from dotenv import load_dotenv                           # Load variables from .env file
import os                                                # Access environment variables
from sqlalchemy import create_engine                     # Create database connection
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()                                            # Read .env file

DB_USER = os.getenv("DB_USER")                           # Get database username
DB_PASSWORD = os.getenv("DB_PASSWORD")                   # Get database password
DB_HOST = os.getenv("DB_HOST")                           # Get database host
DB_NAME = os.getenv("DB_NAME")                           # Get database name
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"  # Build connection string

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()