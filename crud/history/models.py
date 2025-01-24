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
        return f"Persona:  {self.name} {self.last_name} {self.dni}"

class Dr(models.Model):
    id = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()
    
class Consult(models.Model):
    id = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    idDr = models.ForeignKey(Dr, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self) -> str:
        return super().__str__()
    
class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    consult = models.OneToOneField(Consult, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()
    
class Treatment(models.Model):
    id = models.AutoField(primary_key=True)
    consult = models.OneToOneField(Consult, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()
    
