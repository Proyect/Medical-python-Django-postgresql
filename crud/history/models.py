from django.db import models
from person.models import Person
from dr.models import Dr
    
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
    
