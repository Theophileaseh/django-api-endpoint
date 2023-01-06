from django.db import models

class Doctor(models.Model):
  name = models.CharField(max_length=200)
  image = models.CharField(max_length=300)
  specialty = models.CharField(max_length=200)
  bio = models.CharField(max_length=500)


  def __str__(self):
    return self.name + ' ' + ' ' +  self.specialty
