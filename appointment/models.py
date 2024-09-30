from django.db import models
from patient.models import Patient
from doctor.models import Doctor,Availabletime
# Create your models here.
APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

APPOINTMENT_TYPES = [
    ('ONLINE', 'Online'),
    ('OFFLINE', 'Offline'),
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(max_length=10, choices=APPOINTMENT_TYPES, default="Pending")
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS)
    symptom = models.TextField()
    time = models.ForeignKey(Availabletime, on_delete=models.CASCADE)
    cencel = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient: {self.patient.user.first_name} Doctor: {self.doctor.user.first_name}"
