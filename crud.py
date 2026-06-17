from sqlalchemy.orm import Session                      # Import Session type
from models import Employee                             # Import Employee table


def create_employee(db: Session, employee):             # Function to create employee
    new_employee = Employee(                            # Create Employee object
        name=employee.name,                             # Assign name
        email=employee.email,                           # Assign email
        department=employee.department                  # Assign department
    )

    db.add(new_employee)                                # Add record to session
    db.commit()                                         # Save record into MySQL
    db.refresh(new_employee)                            # Reload latest saved data

    return new_employee                                 # Return inserted employee


#----------------------------------------------------------------------------------------------
# READ

def get_employees(db: Session):                         # Get all employees
    return db.query(Employee).all()                     # Select * from employees


#----------------------------------------------------------------------------------

def get_employee_by_id(db: Session, employee_id: int):     # Get employee using id
    return db.query(Employee).filter(                      # Filter records
        Employee.id == employee_id                         # Where id = employee_id
    ).first()                                              # Return first matching row



#----------------------------------------------------------------------------------

def update_employee(db: Session, employee_id: int, employee):   # Update employee
    existing_employee = db.query(Employee).filter(              # Find employee
        Employee.id == employee_id
    ).first()

    existing_employee.name = employee.name                     # Update name
    existing_employee.email = employee.email                   # Update email
    existing_employee.department = employee.department         # Update department

    db.commit()                                                # Save changes
    db.refresh(existing_employee)                              # Reload data

    return existing_employee                                   # Return updated record


#---------------------------------------------------------------------------------------------

def delete_employee(db: Session, employee_id: int):         # Delete employee

    employee = db.query(Employee).filter(                   # Find employee
        Employee.id == employee_id
    ).first()

    db.delete(employee)                                     # Delete record
    db.commit()                                             # Save changes

    return {"message": "Employee deleted successfully"}     # Return message