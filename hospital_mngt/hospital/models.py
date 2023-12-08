from django.db import models



# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Special=models.CharField(max_length=100)


class Patient(models.Model):
    name=models.CharField(max_length=50)
    # gendre=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    address=models.CharField(max_length=100)
      


class Appoinement(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
      return self.Doctor.Name+ "__"+self.Patient.name