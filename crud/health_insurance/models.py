from django.db import models

class Health_insurance(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    observations = models.TextField()
