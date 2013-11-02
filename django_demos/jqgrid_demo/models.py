from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=140)
    age = models.IntegerField()
    weight = models.IntegerField()
    size = models.IntegerField()

    def setReq(self, req=None):
        if req:
            self.name = req.get('name')
            self.age = req.get('age')
            self.weight = req.get('weight')
            self.size = req.get('size')
            
    def __unicode__(self):
        return self.name

