from django.contrib import admin
from appointment.models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name','doctor_name','appointment_status', 'appointment_types','symptom','time','cencel']

    def patient_name(self,obj):
        return obj.patient.user.first_name

    def doctor_name(self, obj):
        return obj.doctor.user.first_name
    
admin.site.register(Appointment, AppointmentAdmin)
