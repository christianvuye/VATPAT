from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
from dashboard.validations import (
    validate_vat, 
    validate_d_id, 
    validate_vat_amounts, 
    validate_total_with_vat, 
    validate_email_date_consistency, 
    validate_month, 
    validate_year, 
    validate_send_date
)

class Dealers(models.Model):
    D_ID = models.CharField(
        max_length=10, 
        unique=True,  
        primary_key=True
        )
    DealerName = models.CharField(max_length=100)
    DealerVATnumber = models.CharField(max_length=20)
    DealerEmail = models.EmailField(max_length=80)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    ModifiedDate = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Dealers'
   
    def clean(self):
        validate_d_id(self.D_ID)
        if not validate_vat(self.DealerVATnumber):
            raise ValidationError({"DealerVATnumber": f"Invalid VAT number: {self.DealerVATnumber}"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self):
        raise IntegrityError("Dealers cannot be deleted")
    
    def __str__(self):
        return (
            f"{self.D_ID}|" 
            f"{self.DealerName}|" 
            f"{self.DealerVATnumber}|" 
            f"{self.DealerEmail}|" 
            f"{self.D_ID}"
        )

class CreditNoteResumeEmail(models.Model):
    CNR_ID = models.AutoField(unique=True, primary_key=True)
    DateIssued = models.DateTimeField(auto_now_add=True)
    Month = models.PositiveIntegerField()
    Year = models.PositiveIntegerField()
    IsValid = models.BooleanField(default=True)
    #CreditNoteResume table should contain a field with the sum of 
    #the total amount of all credit notes for the dealer in the month and year 
    #of the CreditNoteResume

    class Meta:
        db_table = 'CreditNoteResumeEmail'

    def clean(self):
        validate_email_date_consistency(self.Month, self.Year, self.DateIssued)
        validate_month(self.Month)
        validate_year(self.Year)    
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def delete(self):
        raise IntegrityError("CreditNoteResumeEmail cannot be deleted")

    def __str__(self):
        return (
            f"{self.CNR_ID}|" 
            f"{self.DateIssued}|" 
            f"{self.Month}|" 
            f"{self.Year}|" 
            f"{self.IsValid}"
        )

class CreditNotes(models.Model):
    CN_ID = models.CharField(
        max_length=20, 
        unique=True, 
        primary_key=True, 
        default=''
        )

    D_ID = models.ForeignKey(
        Dealers, 
        on_delete=models.CASCADE, 
        db_column='D_ID', 
        default=''
        )
    
    CNR_ID = models.ForeignKey(
        CreditNoteResumeEmail, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='CNR_ID' 
        )
    
    TotalDocumentAmount = models.DecimalField(max_digits=38, decimal_places=20)
    TotalVATAmountDocumentt = models.DecimalField(max_digits=38, decimal_places=20)
    TotalDocumentAmountWithVAT = models.DecimalField(max_digits=38, decimal_places=20)
    AccountingNumberID = models.CharField(max_length=30) #Import from Navision DB, will not change.
    IssuedDate = models.DateTimeField() #Import from Navision DB, will not change.

    class Meta:
        db_table = 'CreditNotes'
    
    def clean(self):
        validate_vat_amounts(self.TotalVATAmountDocumentt, self.TotalDocumentAmount)
        validate_total_with_vat(self.TotalDocumentAmount, self.TotalVATAmountDocumentt, self.TotalDocumentAmountWithVAT)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self):
        raise IntegrityError("CreditNotes cannot be deleted")

    def __str__(self):
        return (
            f"{self.CN_ID}|" 
            f"{self.D_ID}|" 
            f"{self.TotalDocumentAmount}|"
            f"{self.TotalVATAmountDocumentt}|" 
            f"{self.TotalDocumentAmountWithVAT}|" 
            f"{self.AccountingNumberID}|" 
            f"{self.IssuedDate}"
        )

class AcknowledgementRequest(models.Model):
    R_ID = models.AutoField(primary_key=True, unique=True)
    CNR_ID = models.ForeignKey( # send the same request over and over again until it is acknowledged
        CreditNoteResumeEmail, 
        on_delete=models.CASCADE, 
        db_column='CNR_ID',
        default=''
        ) 
    CreatedDate = models.DateTimeField(auto_now_add=True)
    SendDate = models.DateTimeField() #this will store the latest date a reminder has been sent
    RemindersSent = models.PositiveIntegerField(default=0) #this will store the number of reminders sent

    class Meta:
        db_table = 'AcknowledgementRequest'
    
    def clean(self):
        validate_send_date(self.CreatedDate, self.SendDate)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def delete(self):
        raise IntegrityError("AcknowledgementRequest cannot be deleted")
    
    def __str__(self):
        return (
            f"{self.R_ID}|" 
            f"{self.CNR_ID}|" 
            f"{self.CreatedDate}|"
            f"{self.SendDate}"
        )

class AcknowledgementReceived(models.Model):
    A_ID = models.AutoField(primary_key=True, unique=True)
    R_ID = models.ForeignKey(
        AcknowledgementRequest, 
        on_delete=models.CASCADE, 
        db_column='R_ID',
        default=''
        )
    MsgFile = models.BinaryField() #store the email message file

    class Meta:
        db_table = 'AcknowledgementReceived'
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def delete(self):
        raise IntegrityError("AcknowledgementReceived cannot be deleted")
    
    def __str__(self):
        return (
            f"{self.A_ID}|" 
            f"{self.R_ID}"
        )