from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
from dashboard.validations import validate_vat, validate_d_id, validate_vat_amounts, validate_total_with_vat, validate_email_date_consistency, validate_month, validate_year

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
    
    def clean(self):
        # Validate VAT amounts
        validate_vat_amounts(self.TotalVATAmountDocumentt, self.TotalDocumentAmount)

        # Validate TotalDocumentAmountWithVAT is correctly calculated
        validate_total_with_vat(self.TotalDocumentAmount, self.TotalVATAmountDocumentt, self.TotalDocumentAmountWithVAT)
        
    def save(self, *args, **kwargs):
        self.full_clean() # Ensures validation is done before saving
        super().save(*args, **kwargs)

    def delete(self):
        raise IntegrityError("CreditNotes cannot be deleted")

    def __str__(self):
        return f"{self.CN_ID} | {self.D_ID} | {self.TotalDocumentAmount} | {self.TotalVATAmountDocumentt} | {self.TotalDocumentAmountWithVAT} | {self.AccountingNumberID} | {self.IssuedDate}"

class CreditNoteResumeEmail(models.Model):
    CNR_ID = models.AutoField(unique=True, primary_key=True)
    CN_ID = models.ForeignKey(CreditNotes, on_delete=models.CASCADE, db_column='CN_ID')
    DateIssued = models.DateTimeField(auto_now_add=True)
    Month = models.PositiveIntegerField()
    Year = models.PositiveIntegerField()
    Body = models.TextField()
    Subject = models.CharField(max_length=40)
    Status = models.BooleanField()
    IsValid = models.BooleanField(default=True)

    class Meta:
        db_table = 'CreditNoteResumeEmail'

    def clean(self):
        # Validate consistency between DateIssued, Month, and Year
        validate_email_date_consistency(self.Month, self.Year, self.DateIssued)

        # Validate Month
        validate_month(self.Month)

        # Validate Year
        validate_year(self.Year)    
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def delete(self):
        raise IntegrityError("CreditNoteResumeEmail cannot be deleted")

    def __str__(self):
        return f"{self.CNR_ID} | {self.CN_ID} | {self.DateIssued} | {self.Month} | {self.Year} | {self.Body} | {self.Subject} | {self.Status} | {self.IsValid}"

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