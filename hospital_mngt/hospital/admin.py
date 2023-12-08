from django.contrib import admin

from .models import Appoinement, Doctor, Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinement)