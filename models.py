from sqlalchemy import Column, Integer, String           # Column defines table columns, Integer and String define data types
from database import Base                                # Importing parent base class

class Employee(Base):                                    # Employee table class

    __tablename__ = "employees"                          # Actual table name inside MySQL

    id = Column(Integer, primary_key=True, index=True)   # Employee ID, primary key, automatically indexed
    name = Column(String(100))                           # Employee name, maximum 100 characters
    email = Column(String(100))                          # Employee email, maximum 100 characters
    department = Column(String(100))                     # Employee department, maximum 100 characters