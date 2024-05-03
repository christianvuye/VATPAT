from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
from dashboard.validations import validate_vat, validate_d_id

class Dealers(models.Model):
    D_ID = models.CharField(max_length=10, unique=True, validators=[validate_d_id], primary_key=True) 
    DealerName = models.CharField(max_length=100)
    DealerVATnumber = models.CharField(max_length=20)
    DealerEmail = models.EmailField(max_length=80)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    ModifiedDate = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Dealers'

    #remove this clean method and add the validation in the main model class
    #when refactoring the code    
    def clean(self):
        # Validate VAT
        if not validate_vat(self.DealerVATnumber):
            raise ValidationError({"DealerVATnumber": f"Invalid VAT number: {self.DealerVATnumber}"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self):
        raise IntegrityError("Dealers cannot be deleted")
    
    def __str__(self):
        return f"{self.D_ID} | {self.DealerName} | {self.DealerVATnumber} | {self.DealerEmail} | {self.D_ID}"

class CreditNotes(models.Model):
    CN_ID = models.CharField(max_length=20, unique=True, primary_key=True, default='')
    D_ID = models.ForeignKey(Dealers, on_delete=models.CASCADE, db_column='D_ID', default='')
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

    class Meta:
        db_table = 'CreditNoteResumeEmail'

class AcknowledgementRequest(models.Model):
    R_ID = models.AutoField(primary_key=True)
    CNR_ID = models.IntegerField(null=True)
    Status = models.BooleanField()
    CreatedDate = models.DateTimeField()
    SendDate = models.DateTimeField()

    class Meta:
        db_table = 'AcknowledgementRequest'

class AcknowledgementReceived(models.Model):
    A_ID = models.AutoField(primary_key=True, unique=True)
    R_ID = models.IntegerField(null=True)
    MsgFile = models.BinaryField()

    class Meta:
        db_table = 'AcknowledgementReceived'