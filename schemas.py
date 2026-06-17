from pydantic import BaseModel


class EmployeeCreate(BaseModel):                 # Used when creating a new employee

    name: str                                    # Employee name
    email: str                                   # Employee email
    department: str                              # Employee department


#------------------------------------------------------------------------------------------------

class EmployeeUpdate(BaseModel):                         # Schema for updating employee

    name: str                                            # Updated name
    email: str                                           # Updated email
    department: str                                      # Updated department