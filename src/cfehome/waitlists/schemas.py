from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class WaitlistEntryCreateSchema(BaseModel):
    id: str
    email: EmailStr


class WaitlistEntryUpdateSchema(BaseModel):
    email: Optional[EmailStr]  # Email is optional for updates


class WaitlistEntryListSchema(BaseModel):
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime


class WaitlistEntryDetailSchema(BaseModel):
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
