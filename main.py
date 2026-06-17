from fastapi import FastAPI                              # Import FastAPI framework
from database import engine, SessionLocal               # Import database engine and database session
from models import Base                                 # Import Base class used for table creation
from schemas import EmployeeCreate, EmployeeUpdate      # Import request validation schemas

from crud import (create_employee, get_employees, get_employee_by_id, update_employee, delete_employee)                                  # Import CRUD functions

Base.metadata.create_all(bind=engine)                   # Create table if it does not exist

app = FastAPI()                                         # Create FastAPI application


@app.get("/")                                           # Root GET endpoint
def home():

    return {"message": "Employee CRUD API Running"}     # Return simple response


@app.post("/employees")                                 # Create employee endpoint
def add_employee(employee: EmployeeCreate):             # Receive employee data from request body

    db = SessionLocal()                                 # Open database session
    result = create_employee(db, employee)              # Insert employee into database
    db.close()                                          # Close database session

    return result                                       # Return inserted employee details


#-----------------------------------------------------------------------------------------
# READ
@app.get("/employees")                                  # Read all employees
def read_employees():

    db = SessionLocal()                                 # Open database session
    result = get_employees(db)                          # Fetch all employees
    db.close()                                          # Close session

    return result                                       # Return employee list



#---------------------------------------------------------------------------------------------
@app.get("/employees/{employee_id}")                       # Read single employee
def read_employee(employee_id: int):

    db = SessionLocal()                                    # Open database session
    result = get_employee_by_id(db, employee_id)           # Fetch employee
    db.close()                                             # Close session

    return result                                          # Return employee

#--------------------------------------------------------------------------------------------

@app.put("/employees/{employee_id}")                           # Update employee
def edit_employee(employee_id: int, employee: EmployeeUpdate):

    db = SessionLocal()                                        # Open session
    result = update_employee(db, employee_id, employee)        # Update record
    db.close()                                                 # Close session

    return result                                              # Return updated employee


#----------------------------------------------------------------------------------------------

@app.delete("/employees/{employee_id}")                     # Delete employee
def remove_employee(employee_id: int):

    db = SessionLocal()                                     # Open session
    result = delete_employee(db, employee_id)               # Delete record
    db.close()                                              # Close session

    return result                                           # Return message