from django.db import models
import uuid
# Create your models here.


class Patient(models.Model):

    BLOOD_TYPE = [
        ('O+', 'O+'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+')
    ]

    name = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=3, null=True, blank=True)
    blood_group = models.CharField(
        max_length=4, choices=BLOOD_TYPE, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
