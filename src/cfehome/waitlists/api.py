from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from django.utils import timezone

from .schemas import (
    WaitlistEntryListSchema,
    WaitlistEntryDetailSchema,
    WaitlistEntryCreateSchema,
    WaitlistEntryUpdateSchema,
)
from .models import WaitlistEntry

router = Router()


# List all waitlist entries
@router.get("", response=List[WaitlistEntryListSchema], auth=JWTAuth())
def list_waitlist_entries(request):
    entries = WaitlistEntry.objects.all()
    return 200, {
        "status": "success",
        "data": [
            {
                "id": entry.id,
                "email": entry.email,
                "updated": entry.updated.isoformat() if entry.updated else None,
                "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
            }
            for entry in entries
        ],
    }


# Get a specific waitlist entry by ID
@router.get("{entry_id}", response=WaitlistEntryDetailSchema, auth=JWTAuth())
def get_waitlist_entry(request, entry_id: int):
    entry = get_object_or_404(WaitlistEntry, id=entry_id)
    return 200, {
        "status": "success",
        "data": {
            "id": entry.id,
            "email": entry.email,
            "updated": entry.updated.isoformat() if entry.updated else None,
            "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
        },
    }


# Create a new waitlist entry
@router.post("", response=WaitlistEntryDetailSchema, auth=JWTAuth())
def create_waitlist_entry(request, data: WaitlistEntryCreateSchema):
    entry = WaitlistEntry(
        email=data.email,
        updated=timezone.now(),
        timestamp=timezone.now(),
    )
    entry.save()
    return 201, {
        "status": "success",
        "data": {
            "id": entry.id,
            "email": entry.email,
            "updated": entry.updated.isoformat(),
            "timestamp": entry.timestamp.isoformat(),
        },
    }


# Update an existing waitlist entry by ID
@router.put("{entry_id}", response=WaitlistEntryDetailSchema, auth=JWTAuth())
def update_waitlist_entry(request, entry_id: int, data: WaitlistEntryUpdateSchema):
    entry = get_object_or_404(WaitlistEntry, id=entry_id)

    if data.email:
        entry.email = data.email

    entry.updated = timezone.now()
    entry.save()

    return 200, {
        "status": "success",
        "data": {
            "id": entry.id,
            "email": entry.email,
            "updated": entry.updated.isoformat() if entry.updated else None,
            "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
        },
    }


# Delete a waitlist entry by ID
@router.delete("{entry_id}", auth=JWTAuth())
def delete_waitlist_entry(request, entry_id: int):
    entry = get_object_or_404(WaitlistEntry, id=entry_id)
    entry.delete()
    return 204, {"status": "success", "message": "Waitlist entry deleted successfully."}
