import pytest
from django.core.exceptions import ValidationError
from dashboard.models import CreditNotes, Dealers

@pytest.mark.django_db
def test_credit_notes_d_id_not_null(test_credit_note_data, test_dealer_data):
    """
    Test that the D_ID field in the CreditNotes model cannot be empty.
    """
    # Creating a dealer to satisfy foreign key requirement
    dealer = Dealers.objects.create(**test_dealer_data)
    test_credit_note_data['D_ID'] = dealer

    # Attempt to manually set D_ID to None or an invalid value to test model-level validation
    test_credit_note_data['D_ID'] = None  # Simulate the missing D_ID scenario

    credit_note = CreditNotes(**test_credit_note_data)

    # Expecting a ValidationError when full_clean is called
    with pytest.raises(ValidationError) as excinfo:
        credit_note.full_clean()  # This should raise ValidationError for missing D_ID

    # Check that the validation error is due to D_ID being required
    assert 'D_ID' in excinfo.value.error_dict
    assert excinfo.value.error_dict['D_ID'][0].code == 'null'  # or 'blank', based on your validation setup