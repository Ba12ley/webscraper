import uuid
from django.db import models

class DefibLocationNI(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,)
    location_name = models.CharField(max_length=240)
    location_lat = models.CharField(max_length=240)
    location_long = models.CharField(max_length=240)
    date_added = models.DateField(auto_created=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.location_name
