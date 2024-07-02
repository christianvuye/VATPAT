from django.db import models, IntegrityError
from dashboard.validations import (
    validate_vat, 
    validate_d_id, 
    validate_vat_amounts, 
    validate_total_with_vat, 
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
        validate_vat(self.DealerVATnumber)

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


class CreditNoteResume(models.Model):   
    CNR_ID = models.AutoField(unique=True, primary_key=True)
    DateIssued = models.DateTimeField(auto_now_add=True) 
    IsValid = models.BooleanField(default=True)
    TotalCreditNotes =  models.IntegerField(default=0)
    TotalDocumentAmounts = models.DecimalField(default=0, max_digits=38, decimal_places=20)
    TotalVATAmounts = models.DecimalField(default=0,max_digits=38, decimal_places=20)
    TotalDocumentAmountsWithVAT = models.DecimalField(default=0,max_digits=38, decimal_places=20)

    class Meta:
        db_table = 'CreditNoteResume'
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def delete(self):
        raise IntegrityError("CreditNoteResume cannot be deleted")

    def __str__(self): 
        return (
            f"{self.CNR_ID}|" 
            f"{self.DateIssued}|" 
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
        CreditNoteResume, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='CNR_ID' 
        )
    
    #Imported from NavisionDB 
    TotalDocumentAmount = models.DecimalField(max_digits=38, decimal_places=20)
    TotalVATAmountDocumentt = models.DecimalField(max_digits=38, decimal_places=20)
    TotalDocumentAmountWithVAT = models.DecimalField(max_digits=38, decimal_places=20)

    #Imported from NavisionDB
    AccountingNumberID = models.CharField(max_length=30)
    IssuedDate = models.DateTimeField() 

    class Meta:
        db_table = 'CreditNotes'
    
    def clean(self):
        validate_vat_amounts(self.TotalVATAmountDocumentt, self.TotalDocumentAmount)
        validate_total_with_vat(self.TotalDocumentAmount, self.TotalVATAmountDocumentt, self.TotalDocumentAmountWithVAT)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self):
        raise IntegrityError("CreditNote cannot be deleted")

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

    # send the same request over and over again until it is acknowledged, so CNR_ID is constant
    CNR_ID = models.ForeignKey( 
        CreditNoteResume, 
        on_delete=models.CASCADE, 
        db_column='CNR_ID',
        default=''
        )
    
    #stores the date the request was created
    CreatedDate = models.DateTimeField(auto_now_add=True)

    #stores the text content of the email message
    EmailMessage = models.TextField(default='')

    #stores the latest date a reminder has been sent
    SendDate = models.DateTimeField() 

    #stores the number of reminders sent
    RemindersSent = models.PositiveIntegerField(default=0) 

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


class AcknowledgementReceived(models.Model): #check if a response has been received for a request
    A_ID = models.AutoField(primary_key=True, unique=True)
    R_ID = models.ForeignKey(
        AcknowledgementRequest, 
        on_delete=models.CASCADE, 
        db_column='R_ID',
        default='' 
        )

    """
    Why is the email message file stored as a BLOB? 

    Storing it as a BLOB is not recommended. 

    Instead, store the email message file as a text field so that you can query it. 

    BLOB would be for images. 
    """
    MsgFile = models.BinaryField() #this should not be a binary field but a text field so it can be queried

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