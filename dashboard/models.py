from django.db import models

class Dealers(models.Model):
    D_ID = models.CharField(max_length=10, unique=True)
    DealerName = models.CharField(max_length=100)
    DealerVATnumber = models.CharField(max_length=20)
    DealerEmail = models.CharField(max_length=80)
    CreatedDate = models.DateTimeField()
    ModifiedDate = models.DateTimeField()

