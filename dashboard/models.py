from django.db import models

class Dealers(models.Model):
    D_ID = models.CharField(max_length=10, unique=True)
    DealerName = models.CharField(max_length=100)
    DealerVATnumber = models.CharField(max_length=20)
    DealerEmail = models.CharField(max_length=80)
    CreatedDate = models.DateTimeField()
    ModifiedDate = models.DateTimeField()

    class Meta:
        db_table = 'Dealers'

class CreditNotes(models.Model):
    CN_ID = models.CharField(max_length=20, unique=True)
    D_ID = models.ForeignKey(Dealers, on_delete=models.CASCADE, db_column='D_ID')
    TotalDocumentAmount = models.DecimalField(max_digits=38, decimal_places=20)
    TotalVATAmountDocumentt = models.DecimalField(max_digits=38, decimal_places=20)
    TotalDocumentAmountWithVAT = models.DecimalField(max_digits=38, decimal_places=20)
    AccountingNumberID = models.CharField(max_length=30)
    IssuedDate = models.DateTimeField()

    class Meta:
        db_table = 'CreditNotes'

class CreditNoteResumeEmail(models.Model):
    CNR_ID = models.AutoField(primary_key=True)
    CN_ID = models.CharField(max_length=10)
    DateIssued = models.DateTimeField()
    Month = models.IntegerField()
    Year = models.IntegerField()
    Body = models.TextField()
    Subject = models.CharField(max_length=40)
    Status = models.BooleanField()
    IsValid = models.BooleanField()

class AcknowledgementRequest(models.Model):
    R_ID = models.AutoField(primary_key=True)
    CNR_ID = models.IntegerField(null=True)
    Status = models.BooleanField()
    CreatedDate = models.DateTimeField()
    SendDate = models.DateTimeField()

class AcknowledgementReceived(models.Model):
    A_ID = models.AutoField(primary_key=True, unique=True)
    R_ID = models.IntegerField(null=True)
    MsgFile = models.BinaryField()
