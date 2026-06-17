from sqlalchemy import create_engine                      # Used to create connection with MySQL database
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker creates database sessions, declarative_base is parent class for all tables

DATABASE_URL = "mysql+pymysql://root:PASSWORD@localhost/employee_db"  # Connection string containing username, password, host and database name

engine = create_engine(DATABASE_URL)                     # Creates connection engine to communicate with MySQL

SessionLocal = sessionmaker(                             # Creates session factory
    autocommit=False,                                    # Changes are not saved automatically
    autoflush=False,                                     # Changes are not pushed automatically
    bind=engine                                          # Uses the MySQL connection engine
)

Base = declarative_base()                                # Base class used by all database tables