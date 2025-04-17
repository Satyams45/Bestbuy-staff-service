from pydantic import BaseModel

class Staff(BaseModel):
    id: int
    name: str
    position: str
    department: str
    email: str
    phone: str
