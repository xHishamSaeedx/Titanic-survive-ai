from django.db import models
import uuid

sex_choices = (("1","male"),("0","female"))
embark_choices = (("C","Cherbourg"),("Q"," Queenstown"),("S","Southampton"))
pclass_choices = (("1","1st"),("2","2nd"),("3","3rd"))
class data(models.Model):
    name = models.CharField(max_length = 40)
    pclass = models.CharField(max_length = 20, choices = pclass_choices)
    sex = models.CharField(max_length=20,choices = sex_choices)
    age = models.IntegerField()
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    embark = models.CharField(max_length=20,choices = embark_choices)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
# Create your models here.
