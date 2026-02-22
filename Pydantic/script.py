from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Student(BaseModel):
    name: str = Field(min_length=3)
    roll_no: int = Field(gt=0)
    email: Optional[EmailStr] = None
    marks: int = Field(ge=0, le=100)

student = Student(
    name="David",
    roll_no=1,
    email="david@email.com",
    marks=85
)

print(student)