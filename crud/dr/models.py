from django.db import models
from person.models import Person

class Dr(models.Model):
    id = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()

