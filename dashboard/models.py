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

"""
Evaluate suggested changes to the models to be made by the following criteria:

1. Necessity: Is the change essential for core functionality, bug fixes, or project requirements?

2. Impact: Does the change break existing functionality or require significant modifications?

3. Complexity: Can the change be implemented within the remaining time without introducing significant complexity?

4. Performance: Does the change improve performance, such as optimizing database queries?

5. User Experience: Does the change enhance user experience or provide business value?

6. Testing: Can the change be thoroughly tested and validated within the available time?

7. Maintainability: Is the change well-documented and easy to understand for future maintenance?
"""

"""
Classes that refer to one object, such as a dealer, should be singular. 

Therefore, the class name should be Dealer instead of Dealers. CreditNotes should be CreditNote.

Evaluation criteria for change:
1. Necessity: It is not essential for core functionality, bug fixes, or project requirements.
2. Impact: It will break existing functionality and require significant modifications.
3. Complexity: It will introduce some complexity.
4. Performance: Unknown.
5. User Experience: It will not enhance user experience or provide business value.
6. Testing: No time to thoroughly test and validate.
7. Maintainability: It will make the code easier to maintain in the future.

Based on the evaluation criteria, the change is not recommended.
"""

"""
PIP Install Flake8 to enforce PEP-8 style guide in the code.

Evaluation criteria for change:
1. Necessity: It is not essential for core functionality, bug fixes, or project requirements.

2. Impact: It will not break existing functionality and will not require significant modifications.

3. Complexity: It will introduce some extra complexity.

4. Performance: Unknown.

5. User Experience: It will not enhance user experience or provide business value.

6. Testing: No time to thoroughly test and validate.

7. Maintainability: It will make the code easier to maintain in the future.

Based on the evaluation criteria, the change is not recommended for now. 
"""

"""
By PEP-8 standards, variable names should be lowercase with underscores between words.

To maintain the PEP-8 standard, use the db_column parameter to map to the name of the column in the database.

Evaluation criteria for change:
1. Necessity: It is not essential for core functionality, bug fixes, or project requirements.

2. Impact: It will not existing functionality and will require some modifications.

3. Complexity: It will introduce some complexity.

4. Performance: Unknown.

5. User Experience: It will not enhance user experience or provide business value.

6. Testing: No time to thoroughly test and validate.

7. Maintainability: It will make the code more readable and easier to maintain in the future.

Based on the evaluation criteria, the change is not recommended for now.
"""
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
    
    """
    String method should only return the most important fields, not all of them. 

    The character limit for the string method should be around 20-30 characters.

    Evaluation criteria for change:

    1. Necessity: It is not essential for core functionality, bug fixes, or project requirements.

    2. Impact: It will not break existing functionality and will not require significant modifications.

    3. Complexity: It will not introduce any complexity.

    4. Performance: Unknown.

    5. User Experience: It will not enhance user experience or provide business value.

    6. Testing: No time to thoroughly test and validate.

    7. Maintainability: It will make the code easier to maintain in the future.

    Based on the evaluation criteria, the change is not recommended for now.
    """
    def __str__(self): 
        return (
            f"{self.D_ID}|" 
            f"{self.DealerName}|" 
            f"{self.DealerVATnumber}|" 
            f"{self.DealerEmail}|" 
            f"{self.D_ID}"
        )


class CreditNoteResumeEmail(models.Model): #change name to CreditNoteResume object -> is it worth it? 
    """
    Should the CreditNoteResume table contain a field with the sum of 
    the total amount(s) of all the aggregated credit notes for that dealer in that month? 
    """
    CNR_ID = models.AutoField(unique=True, primary_key=True)
    DateIssued = models.DateTimeField(auto_now_add=True) #keep this and remove month and year fields
    Month = models.PositiveIntegerField() #use datefield so that you don't have to make conversions to integer and vice versa
    Year = models.PositiveIntegerField() #have a datefield with both month and year instead of two seperate fields
    IsValid = models.BooleanField(default=True) #needs to be evaluated by Jessamyn 

    class Meta:
        db_table = 'CreditNoteResumeEmail'

    def clean(self):
        validate_email_date_consistency(self.Month, self.Year, self.DateIssued)
        validate_month(self.Month) #no need for this 
        validate_year(self.Year) #no need for this either
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def delete(self):
        raise IntegrityError("CreditNoteResumeEmail cannot be deleted")

    def __str__(self): #do you need all the fields in the string method? Probably not. 
        return (
            f"{self.CNR_ID}|" 
            f"{self.DateIssued}|" 
            f"{self.Month}|" 
            f"{self.Year}|" 
            f"{self.IsValid}"
        )


#python classes can inherit from multiple classes
#Mixin class -> use this to avoid repeating the same code in multiple classes
class CreditNotes(models.Model):   
    CN_ID = models.CharField(
        max_length=20, 
        unique=True, 
        primary_key=True, 
        default='' #why is this set to default empty string? There are no empty strings in the db for this field, see what happens when you remove this
        )

    D_ID = models.ForeignKey(
        Dealers, 
        on_delete=models.CASCADE, 
        db_column='D_ID', 
        default='' #why is this set to default empty string? There are no empty strings in the db for this field, see what happens when you remove this
        )
    
    CNR_ID = models.ForeignKey(
        CreditNoteResumeEmail, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='CNR_ID' 
        )
    
    #these fields are imported from the Navision DB as well 
    TotalDocumentAmount = models.DecimalField(max_digits=38, decimal_places=20)
    TotalVATAmountDocumentt = models.DecimalField(max_digits=38, decimal_places=20)
    TotalDocumentAmountWithVAT = models.DecimalField(max_digits=38, decimal_places=20)

    #The fields below will be imported from the Navision DB and will not change.
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
        raise IntegrityError("CreditNoteResume cannot be deleted") # create a parent class that has all the common methods and inherit from it

    def __str__(self): #less fields in the string method -> only the most important ones, not more than 20 or 30
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
        CreditNoteResumeEmail, 
        on_delete=models.CASCADE, 
        db_column='CNR_ID',
        default='' #why is this set to default empty string? There are no empty strings in the db for this field, see what happens when you remove this
        ) 
    CreatedDate = models.DateTimeField(auto_now_add=True)

    #this will store the latest date a reminder has been sent
    SendDate = models.DateTimeField() 

    #this will store the number of reminders sent
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
    
    def __str__(self): #less fields in the string method -> only the most important ones, not more than 20 or 30
        return (
            f"{self.R_ID}|" 
            f"{self.CNR_ID}|" 
            f"{self.CreatedDate}|"
            f"{self.SendDate}"
        )


class AcknowledgementReceived(models.Model): #we check if a response has been received for a request
    A_ID = models.AutoField(primary_key=True, unique=True)
    R_ID = models.ForeignKey(
        AcknowledgementRequest, 
        on_delete=models.CASCADE, 
        db_column='R_ID',
        default=''
        )

    #store the email message file
    #storing it as a BLOB -> BLOB would be for images, use a text field instead, then you can query it
    MsgFile = models.BinaryField() #why is this a binary field? This should be a text field than you can query it. 

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