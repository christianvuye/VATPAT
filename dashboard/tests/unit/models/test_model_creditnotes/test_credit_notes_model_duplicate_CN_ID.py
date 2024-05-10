import pytest
from django.core.exceptions import ValidationError
from dashboard.models import CreditNotes, Dealers
from decimal import Decimal

@pytest.mark.django_db
def test_credit_notes_cn_id_unique_model_level(test_dealer_data, test_credit_note_data):
    """
    Test that the CN_ID field in the CreditNotes model is unique at the model level.
    """
    # Creating a dealer to satisfy foreign key requirement
    dealer = Dealers.objects.create(**test_dealer_data)

    # Create the first CreditNotes instance
    first_credit_note = CreditNotes(
        **test_credit_note_data,
        D_ID=dealer
    )
    first_credit_note.full_clean()
    first_credit_note.save()

    # Modify test_credit_note_data for the second instance
    test_credit_note_data.update({
        'TotalDocumentAmount': Decimal('5678.90'),
        'TotalVATAmountDocumentt': Decimal('678.90'),
        'TotalDocumentAmountWithVAT': Decimal('7357.80'),
        'AccountingNumberID': "AC0987654321"
    })

    # Prepare a second CreditNotes instance with the same CN_ID
    second_credit_note = CreditNotes(
        **test_credit_note_data,
        D_ID=dealer,
    )

    # Attempt to validate the second instance using full_clean
    with pytest.raises(ValidationError) as excinfo:
        second_credit_note.full_clean()

    # Check that the validation error is due to the unique constraint on CN_ID
    assert 'CN_ID' in excinfo.value.error_dict
    assert 'already exists' in excinfo.value.error_dict['CN_ID'][0].message