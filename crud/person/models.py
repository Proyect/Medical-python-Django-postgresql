from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    last_name = models.TextField()
    dni = models.TextField()
    birth_date = models.DateField()
    gender = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    address = models.TextField()
    observations = models.TextField()

    def __str__(self) -> str:
        return f"Persona:  {self.name} {self.last_name} {self.dni} {self.phone} {self.email}"
