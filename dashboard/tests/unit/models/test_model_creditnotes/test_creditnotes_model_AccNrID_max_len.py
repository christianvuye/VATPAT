import pytest
from django.core.exceptions import ValidationError
from dashboard.models import CreditNotes, Dealers

@pytest.mark.django_db
def test_credit_notes_accounting_number_id_max_length(test_dealer_data, test_credit_note_data):
    """
    Test that the AccountingNumberID field does not accept values longer than its max_length.
    """
    dealer = Dealers.objects.create(**test_dealer_data)
    test_credit_note_data['D_ID'] = dealer

    # Assign an AccountingNumberID value that exceeds the max_length
    test_credit_note_data['AccountingNumberID'] = 'A' * 31  # max_length is 30

    # Expecting a ValidationError when trying to save a too long AccountingNumberID
    with pytest.raises(ValidationError):
        credit_note = CreditNotes(**test_credit_note_data)
        credit_note.full_clean()  # This should raise ValidationError