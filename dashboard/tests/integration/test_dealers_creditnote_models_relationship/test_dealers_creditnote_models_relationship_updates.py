import pytest
from django.utils import timezone
from dashboard.models import CreditNotes, Dealers

@pytest.fixture
def dummy_dealer_and_credit_note():
    # Create a dummy Dealer instance
    dealer = Dealers.objects.create(
        D_ID="D001",
        DealerName="Dummy Dealer",
        DealerVATnumber="538046554",
        DealerEmail="dummydealer@example.com",
        CreatedDate=timezone.now(),
        ModifiedDate=timezone.now()
    )

    # Create a dummy CreditNote instance
    credit_note = CreditNotes.objects.create(
        CN_ID="CN001",
        D_ID=dealer,  # Reference the dummy dealer instance
        TotalDocumentAmount=12345.67,
        TotalVATAmountDocumentt=1234.56,
        TotalDocumentAmountWithVAT=13580.23,
        AccountingNumberID="AN12345",
        IssuedDate=timezone.now()
    )

    return dealer, credit_note

@pytest.mark.django_db
def test_dealers_creditnote_models_relationship_updates(dummy_dealer_and_credit_note):
    dealer, credit_note = dummy_dealer_and_credit_note

    # Update all fields of the dealer
    dealer.DealerName = "Updated Dealer"
    dealer.DealerVATnumber = "225616009"
    dealer.DealerEmail = "updatedemail@example.com"
    updated_created_date = timezone.now()
    dealer.CreatedDate = updated_created_date
    dealer.save()
    updated_modified_date = dealer.ModifiedDate  # Get the ModifiedDate after saving

    # Refresh the credit_note instance from the database
    credit_note.refresh_from_db()

    # Assert that the credit note still references the updated dealer
    assert credit_note.D_ID == dealer, "CreditNote does not reference the updated Dealer instance"

    # Verify individual fields have been updated
    assert credit_note.D_ID.DealerName == dealer.DealerName, "CreditNote's DealerName did not update correctly"
    assert credit_note.D_ID.DealerVATnumber == dealer.DealerVATnumber, "CreditNote's DealerVATnumber did not update correctly"
    assert credit_note.D_ID.DealerEmail == dealer.DealerEmail, "CreditNote's DealerEmail did not update correctly"
    assert credit_note.D_ID.CreatedDate == updated_created_date, "CreditNote's Dealer CreatedDate did not update correctly"
    assert credit_note.D_ID.ModifiedDate == updated_modified_date, "CreditNote's Dealer ModifiedDate did not update correctly"

    # Verify ModifiedDate is approximately equal to updated_modified_date
    # This is a simple way to compare the dates with some flexibility. You might need to adjust the delta.
    assert abs((credit_note.D_ID.ModifiedDate - updated_modified_date).total_seconds()) < 1, "CreditNote's Dealer ModifiedDate did not update correctly"