from fastapi import APIRouter, HTTPException
from typing import List
from models import Staff

router = APIRouter(prefix="/staff", tags=["Staff"])

# In-memory staff database
staff_db: List[Staff] = [
    Staff(
        id=1,
        name="Alice Johnson",
        position="Sales Manager",
        department="Sales",
        email="alice.johnson@bestbuy.com",
        phone="123-456-7890"
    ),
    Staff(
        id=2,
        name="Bob Smith",
        position="IT Specialist",
        department="IT",
        email="bob.smith@bestbuy.com",
        phone="234-567-8901"
    ),
    Staff(
        id=3,
        name="Charlie Nguyen",
        position="Customer Service Rep",
        department="Support",
        email="charlie.nguyen@bestbuy.com",
        phone="345-678-9012"
    )
]

# Get all staff
@router.get("/", response_model=List[Staff])
def get_all_staff():
    return staff_db

# Get a single staff member by ID
@router.get("/{staff_id}", response_model=Staff)
def get_staff(staff_id: int):
    for staff in staff_db:
        if staff.id == staff_id:
            return staff
    raise HTTPException(status_code=404, detail="Staff not found")

# Create new staff
@router.post("/", response_model=Staff)
def create_staff(staff: Staff):
    staff_db.append(staff)
    return staff

# Update staff info
@router.put("/{staff_id}", response_model=Staff)
def update_staff(staff_id: int, updated_staff: Staff):
    for index, staff in enumerate(staff_db):
        if staff.id == staff_id:
            staff_db[index] = updated_staff
            return updated_staff
    raise HTTPException(status_code=404, detail="Staff not found")

# Delete staff
@router.delete("/{staff_id}")
def delete_staff(staff_id: int):
    for index, staff in enumerate(staff_db):
        if staff.id == staff_id:
            staff_db.pop(index)
            return {"message": "Staff deleted"}
    raise HTTPException(status_code=404, detail="Staff not found")
