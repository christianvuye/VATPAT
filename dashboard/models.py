from django.db import models

class Dealers(models.Model):
    D_ID = models.CharField(max_length=10, unique=True)
    DealerName = models.CharField(max_length=100)
    DealerVATnumber = models.CharField(max_length=20)
    DealerEmail = models.CharField(max_length=80)
    CreatedDate = models.DateTimeField()
    ModifiedDate = models.DateTimeField()

class CreditNotes(models.Model):
    CN_ID = models.CharField(max_length=20, unique=True)
    D_ID = models.CharField(max_length=10)
    TotalDocumentAmount = models.DecimalField(max_digits=38, decimal_places=20)
    TotalVATAmountDocumentt = models.DecimalField(max_digits=38, decimal_places=20)
    TotalDocumentAmountWithVAT = models.DecimalField(max_digits=38, decimal_places=20)
    AccountingNumberID = models.CharField(max_length=30)
    IssuedDate = models.DateTimeField()

class CreditNoteResumeEmail(models.Model):
    pass