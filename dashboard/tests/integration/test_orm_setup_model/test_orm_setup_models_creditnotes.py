import pytest
from django.utils import timezone
from dashboard.models import CreditNotes, Dealers 

@pytest.fixture
def create_credit_note():
    now = timezone.now()  # timezone-aware datetime for the IssuedDate

    # Create an instance of the Dealers model with sample data
    dealer_instance = Dealers.objects.create(
        D_ID='PT123456',
        DealerName='Sample Dealer',
        DealerVATnumber='229986358',
        DealerEmail='dealer@example.com',
        CreatedDate=now,
        ModifiedDate=now
    )

    return CreditNotes.objects.create(
        CN_ID='CN001',
        D_ID=dealer_instance,
        TotalDocumentAmount=12345.67,
        TotalVATAmountDocumentt=1234.56,
        TotalDocumentAmountWithVAT=13580.23,
        AccountingNumberID='AN12345',
        IssuedDate=now
    )

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_credit_notes(create_credit_note):
    all_credit_notes = CreditNotes.objects.all()

    # Ensure we can fetch credit notes, indicating no basic mismatch
    assert all_credit_notes.exists(), "Failed to fetch credit notes from the database."
    assert create_credit_note in all_credit_notes, "Created credit note is not in the database."
