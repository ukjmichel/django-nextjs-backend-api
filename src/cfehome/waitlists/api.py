from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from django.utils import timezone

from .schemas import (
    WaitlistEntryListSchema,
    WaitlistEntryDetailSchema,
    WaitlistEntryCreateSchema,
)
from .models import WaitlistEntry


router = Router()


@router.get("", response=List[WaitlistEntryListSchema], auth=JWTAuth())
def list_waitlist_entries(request):
    # Fetch all waitlist entries from the database
    entries = WaitlistEntry.objects.all()

    # Return a list of serialized entries
    return [
        {
            "id": entry.id,
            "email": entry.email,
            "updated": entry.updated.isoformat() if entry.updated else None,
            "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
        }
        for entry in entries
    ]


@router.get("{entry_id}", response=WaitlistEntryDetailSchema, auth=JWTAuth())
def get_waitlist_entry(request, entry_id: int):
    # Retrieve a specific waitlist entry or return a 404 if not found
    entry = get_object_or_404(WaitlistEntry, id=entry_id)

    # Return the serialized entry data
    return {
        "id": entry.id,
        "email": entry.email,
        "updated": entry.updated.isoformat() if entry.updated else None,
        "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
    }


@router.post("", response=WaitlistEntryDetailSchema, auth=JWTAuth())
def create_waitlist_entry(request, data: WaitlistEntryCreateSchema):
    # Create a WaitlistEntry instance with current date and time for updated and timestamp
    entry = WaitlistEntry(
        id=data.id,
        email=data.email,
        updated=timezone.now(),  # Set current datetime
        timestamp=timezone.now(),  # Set current datetime
    )
    entry.save()
    return entry
