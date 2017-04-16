from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    medical_center = models.CharField(max_length=30, blank=True)



class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank = True)
    index = models.ForeignKey(User)
    ethnicity = models.CharField(max_length=15)
    weight = models.CharField(max_length=6)
    height = models.CharField(max_length=4)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=5, default='')


class Note(models.Model):
    PERSCRIPTION='Prescription'
    BLOODWORK='Bloodwork'
    ALLERGIES='Allergy'
    CT='CT'
    EXTRA_NOTES="Additional Notes"
    OPTIONS = (
    (PERSCRIPTION, "Prescription"),
    (BLOODWORK, "Bloodwork"),
    (ALLERGIES, "Allergy"),
    (CT,"Cat Scan"),
    (EXTRA_NOTES, "Additional Notes"),
    )



    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note = models.CharField(max_length=16)
    message = models.CharField(max_length=100)
    note_type = models.CharField(max_length=30, choices = OPTIONS, default = EXTRA_NOTES)
    date_started = models.DateField('date start')
    date_ended = models.DateField('date end')
    last_modified = models.DateField(auto_now=True)
