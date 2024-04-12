import pytest
from django.utils import timezone
from dashboard.models import Dealers, CreditNotes

@pytest.mark.django_db
def test_dealers_creditnote_impact(test_dealer_data_with_credit_note):
    """
    Test that updates to Dealer attributes (name, VAT number, and email)
    do not affect the financial details of the related CreditNotes.
    """
    # Create the dealer using the fixture data
    dealer = Dealers.objects.create(**test_dealer_data_with_credit_note)
    
    # Create a related CreditNote
    credit_note = CreditNotes.objects.create(
        CN_ID="CN0001",
        D_ID=dealer,
        TotalDocumentAmount=1000.00,
        TotalVATAmountDocumentt=150.00,
        TotalDocumentAmountWithVAT=1150.00,
        AccountingNumberID="ACC123456",
        IssuedDate=timezone.now(),
    )

    # Capture the initial state of the related CreditNote
    initial_values = {
        "TotalDocumentAmount": credit_note.TotalDocumentAmount,
        "TotalVATAmountDocumentt": credit_note.TotalVATAmountDocumentt,
        "TotalDocumentAmountWithVAT": credit_note.TotalDocumentAmountWithVAT,
    }

    # Update the Dealer
    dealer.DealerName = "Updated Dealer Name"
    dealer.DealerVATnumber = "253512182"
    dealer.DealerEmail = "updated_dealer@example.com"
    dealer.save()

    # Re-fetch the CreditNote to ensure it hasn't changed
    credit_note.refresh_from_db()
    updated_values = {
        "TotalDocumentAmount": credit_note.TotalDocumentAmount,
        "TotalVATAmountDocumentt": credit_note.TotalVATAmountDocumentt,
        "TotalDocumentAmountWithVAT": credit_note.TotalDocumentAmountWithVAT,
    }

    assert initial_values == updated_values, "CreditNote details should remain unchanged after updating Dealer."
