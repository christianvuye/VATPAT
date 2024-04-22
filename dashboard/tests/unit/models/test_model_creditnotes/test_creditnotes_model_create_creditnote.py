import pytest
from dashboard.models import CreditNotes, Dealers
from decimal import Decimal
from django.utils import timezone

@pytest.mark.django_db
def test_creditnotes_model_create_creditnote(test_dealer_data, test_credit_note_data):
    """
    Test the creation of a CreditNote with a newly created dealer instance.
    """
    # Creating a dealer instance first
    dealer = Dealers.objects.create(**test_dealer_data)

    # Update the dealer ID in credit note data
    test_credit_note_data['D_ID'] = dealer  # Assign the dealer instance

    # Create the credit note
    credit_note = CreditNotes.objects.create(**test_credit_note_data)

    # Asserting that the credit note is created with the correct dealer
    assert credit_note.D_ID == dealer
    assert credit_note.CN_ID == "CN20230001"
    assert credit_note.TotalDocumentAmount == Decimal('1234.56')
    assert credit_note.TotalVATAmountDocumentt == Decimal('234.56')
    assert credit_note.TotalDocumentAmountWithVAT == Decimal('1469.13')
    assert credit_note.AccountingNumberID == "AC1234567890"
    assert credit_note.IssuedDate.date() == timezone.now().date() # Asserting the date only since the time will be slightly different

    # Asserting dealer details are correctly assigned
    assert dealer.D_ID == test_dealer_data['D_ID']
    assert dealer.DealerName == test_dealer_data['DealerName']
    assert dealer.DealerVATnumber == test_dealer_data['DealerVATnumber']
    assert dealer.DealerEmail == test_dealer_data['DealerEmail']
    assert dealer.CreatedDate.date() == test_dealer_data['CreatedDate'].date() # Asserting the date only since the time will be slightly different
    assert dealer.ModifiedDate.date() == test_dealer_data['ModifiedDate'].date() # Asserting the date only since the time will be slightly different
    assert dealer.is_active == test_dealer_data['is_active']