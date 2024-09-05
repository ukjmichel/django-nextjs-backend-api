from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router


from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema
from .models import WaitlistEntry


router = Router()


@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    entries = WaitlistEntry.objects.all()
    return [
        {
            "id": entry.id,
            "email": entry.email,
            "updated": entry.updated.isoformat() if entry.updated else None,
            "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
        }
        for entry in entries
    ]


@router.get("{entry_id}", response=WaitlistEntryDetailSchema)
def get_waitlist_entry(request, entry_id: int):
    # Use get_object_or_404 to retrieve the specific entry or return a 404 error if not found
    entry = get_object_or_404(WaitlistEntry, id=entry_id)

    return {
        "id": entry.id,
        "email": entry.email,
        "updated": entry.updated.isoformat() if entry.updated else None,
        "timestamp": entry.timestamp.isoformat() if entry.timestamp else None,
    }
