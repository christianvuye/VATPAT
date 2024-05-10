import pytest
from decimal import Decimal
from django.utils import timezone

@pytest.fixture
def test_dealer_data():
    """Fixture to provide dealer data dictionary."""
    return {
        "D_ID": "PT123456",
        "DealerName": "Test Dealer",
        "DealerVATnumber": "253512182",
        "DealerEmail": "dealer@example.com",
        "CreatedDate": timezone.now(),
        "ModifiedDate": timezone.now(),
        "is_active": True
    }

@pytest.fixture
def test_credit_note_data():
    """
    Fixture to provide credit note data dictionary.
    """
    return {
        "CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        "TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.12'),
        "AccountingNumberID": "AC1234567890", 
        "IssuedDate": timezone.now()
    }

@pytest.fixture
def test_credit_note_data_missing_cn_id():
    """
    Fixture to provide credit note data dictionary with missing CN_ID.
    """
    return {
        #"CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        "TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.12'),
        "AccountingNumberID": "AC1234567890", 
        "IssuedDate": timezone.now()
    }

@pytest.fixture
def test_credit_note_data_missing_total_document_amount():
    """
    Fixture to provide credit note data dictionary with missing TotalDocumentAmount.
    """
    return {
        "CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        #"TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.12'),
        "AccountingNumberID": "AC1234567890", 
        "IssuedDate": timezone.now()
    }

@pytest.fixture
def test_credit_note_data_missing_total_vat_amount_document():
    """
    Fixture to provide credit note data dictionary with missing TotalVATAmountDocumentt.
    """
    return {
        "CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        "TotalDocumentAmount": Decimal('1234.56'),
        #"TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.12'),
        "AccountingNumberID": "AC1234567890", 
        "IssuedDate": timezone.now()
    }

@pytest.fixture
def test_credit_note_data_missing_total_document_amount_with_vat():
    """
    Fixture to provide credit note data dictionary with missing TotalDocumentAmountWithVAT.
    """
    return {
        "CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        "TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        #"TotalDocumentAmountWithVAT": Decimal('1469.12'),
        "AccountingNumberID": "AC1234567890", 
        "IssuedDate": timezone.now()
    }

@pytest.fixture
def test_credit_note_data_missing_accounting_number_id():
    """
    Fixture to provide credit note data dictionary with missing AccountingNumberID.
    """
    return {
        "CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        "TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.12'),
        #"AccountingNumberID": "AC1234567890", 
        "IssuedDate": timezone.now()
    }

@pytest.fixture
def test_credit_note_data_missing_issued_date():
    """
    Fixture to provide credit note data dictionary with missing IssuedDate.
    """
    return {
        "CN_ID": "CN20230001", 
        #"D_ID": "PT123456", Omit the D_ID since it will be set to the dealer created during tests.
        "TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.12'),
        "AccountingNumberID": "AC1234567890", 
        #"IssuedDate": timezone.now()
    }