from ninja import Schema
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic import EmailStr


class WaitlistEntryCreateSchema(BaseModel):
    id: str
    email: EmailStr


class WaitlistEntryListSchema(Schema):
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime


class WaitlistEntryDetailSchema(Schema):
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
