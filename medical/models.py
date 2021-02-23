from django.db import models

# Create your models here.


class MedicalStore(models.Model):
    name = models.CharField(max_length=200)
    box_qty = models.IntegerField()
    qty = models.IntegerField()
    expired_date = models.DateField()

    def __str__(self):
        return self.name
