import pytest
from django.db.utils import IntegrityError
from dashboard.models import CreditNotes, Dealers

@pytest.mark.django_db
def test_creditnotes_model_duplicate_cn_id(test_dealer_data, test_credit_note_data):
    """
    Test that creating a credit note with a duplicate CN_ID raises an error
    on the database level - IntegrityError.
    """
    # Creating a dealer instance first
    dealer = Dealers.objects.create(**test_dealer_data)

    # Assign the dealer instance to the credit note data
    test_credit_note_data['D_ID'] = dealer

    # Create the first credit note
    CreditNotes.objects.create(**test_credit_note_data)

    # Attempt to create a second credit note with the same CN_ID
    with pytest.raises(IntegrityError):
        CreditNotes.objects.create(**test_credit_note_data)