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
    }

@pytest.fixture
def test_credit_note_data():
    """
    Fixture to provide credit note data dictionary.
    """
    return {
        "CN_ID": "CN20230001", #Check with Paulo if this is the correct format
        "D_ID": "PT123456", #References the dealer above
        "TotalDocumentAmount": Decimal('1234.56'),
        "TotalVATAmountDocumentt": Decimal('234.56'),
        "TotalDocumentAmountWithVAT": Decimal('1469.13'),
        "AccountingNumberID": "AC1234567890", #Check with Paulo if this is the correct format
        "IssuedDate": timezone.now()
    }