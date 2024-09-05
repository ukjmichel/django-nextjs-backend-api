from django.db import models


# Create your models here.
class WaitlistEntry(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True
    )  # Ensure this field exists if you need it

    def __str__(self):
        return self.email
