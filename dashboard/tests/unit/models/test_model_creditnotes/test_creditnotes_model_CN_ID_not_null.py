import pytest
from django.core.exceptions import ValidationError
from dashboard.models import CreditNotes, Dealers

@pytest.mark.django_db
def test_creditnotes_model_CN_ID_not_null(test_dealer_data, test_credit_note_data_missing_cn_id):
    """
    Test that the CN_ID field is not nullable.
    """
    dealer = Dealers.objects.create(**test_dealer_data)
    test_credit_note_data_missing_cn_id['D_ID'] = dealer

    # Try to create a CreditNotes instance with missing CN_ID
    with pytest.raises(ValidationError) as e:
        credit_note = CreditNotes(**test_credit_note_data_missing_cn_id)
        credit_note.full_clean()  # This should raise ValidationError

    # Check that the validation error is due to CN_ID being required
    assert 'CN_ID' in e.value.error_dict
    assert e.value.error_dict['CN_ID'][0].code == 'blank'