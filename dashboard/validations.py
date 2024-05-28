import re
from django.core.exceptions import ValidationError
"""
The algorithm to verify the NIF number in Portugal is as follows:

Ensure the number has 9 digits.

Multiply each of the first 8 digits by a decreasing sequence of multipliers,
starting from 9 (i.e., 9, 8, 7, 6, 5, 4, 3, 2).

Sum the results of these multiplications.

Calculate the remainder of dividing this sum by 11.

If the remainder is 0 or 1, the check digit should be 0. 
Otherwise, subtract the remainder from 11 to get the check digit.

Compare the calculated check digit with the actual ninth digit 
of the NIF number to verify its validity.
"""


"""
NIF numbers (Número de Identificação Fiscal) in Portugal cannot start with a 0. 

Prefixes: The first digit of a NIF number indicates the type of taxpayer:

1: Pessoa singular (individuals)
2: Pessoa singular (individuals)
3: Pessoa singular (individuals) - new from 2019
5: Pessoa coletiva (businesses)
6: Pessoa coletiva (public entities)
8: Empresário em nome individual (sole traders)
9: Pessoa colectiva irregular ou numero provisorio (temporary numbers)

"""

def validate_vat(vat):
    """
    Validates the Portuguese VAT number (NIF) using the algorithm described above.
    """
    # Ensure VAT is a string to handle leading zeros
    vat = str(vat)
    
    # Check if VAT has exactly 9 digits
    if len(vat) != 9:
        raise ValidationError("VAT number must have 9 digits.")

    # Check if VAT has only digits
    if not vat.isdigit():
        raise ValidationError("VAT number must contain only digits.")

    # Check if the first digit is one of the allowed prefixes
    if vat[0] not in ["1", "2", "3", "5", "6", "8", "9"]:
        raise ValidationError("Prefix of VAT number is invalid.")
    
    # Define the sequence of multipliers
    multipliers = [9, 8, 7, 6, 5, 4, 3, 2]
    
    # Calculate the checksum
    checksum = 0
    for i in range(8):
        checksum += int(vat[i]) * multipliers[i]    
    
    # Calculate the remainder of the checksum divided by 11
    remainder = checksum % 11
    
    # Determine the check digit
    if remainder < 2:
        check_digit = 0
    else:
        check_digit = 11 - remainder
       
    # Verify if the last digit matches the check digit
    is_valid = int(vat[-1]) == check_digit

    if not is_valid:
        raise ValidationError("Invalid VAT number.")

def validate_d_id(d_id):
    # Regular expression to match the required D_ID format
    d_id_regex = re.compile(r'^PT\d{6}$')

    if not d_id_regex.match(d_id):
        raise ValidationError("D_ID must start with 'PT' followed by 6 digits.")

def validate_vat_amounts(TotalVATAmountDocumentt, TotalDocumentAmount):
    """
    Validates that the VAT amount does not exceed the total document amount.
    
    Args:
    TotalVATAmountDocument (Decimal): The VAT amount on the document.
    TotalDocumentAmount (Decimal): The total amount of the document.

    Raises:
    ValidationError: If the VAT amount exceeds the total document amount.
    """
    if TotalVATAmountDocumentt > TotalDocumentAmount:
        raise ValidationError("The VAT amount cannot exceed the total document amount.")

def validate_total_with_vat(TotalDocumentAmount, TotalVATAmountDocumentt, TotalDocumentAmountWithVAT):
    """
    Validates that the total amount with VAT is the sum of the total amount and the VAT amount.

    Args:
    TotalDocumentAmount (Decimal): The total amount of the document.
    TotalVATAmountDocument (Decimal): The VAT amount on the document.
    TotalDocumentAmountWithVAT (Decimal): The total amount with VAT.

    Raises:
    ValidationError: If the total amount with VAT does not match the sum of the total amount and the VAT amount.
    """
    if TotalDocumentAmount + TotalVATAmountDocumentt != TotalDocumentAmountWithVAT:
        raise ValidationError("The total amount with VAT must be the sum of the total amount and the VAT amount.")
    
def validate_email_date_consistency(month, year, date_issued):
    """
    Validates that the Month and Year fields correspond to the DateIssued.
    
    Args:
    month (int): Month extracted from DateIssued.
    year (int): Year extracted from DateIssued.
    date_issued (datetime): Date when the email was issued.
    
    Raises:
    ValidationError: If Month and Year do not match those of DateIssued.
    """
    if date_issued.month != month or date_issued.year != year:
        raise ValidationError("Month and Year must match the date the email was issued.")

def validate_month(month):
    if month < 1 or month > 12:
        raise ValidationError("Month must be between 1 and 12.")
    
def validate_year(year):
    if year < 2000 or year > 2050:
        raise ValidationError("Year must be between 2000 and 2050.")

def validate_send_date(created_date, send_date):
    if send_date < created_date:
        raise ValidationError("Send date cannot be earlier than the created date.")