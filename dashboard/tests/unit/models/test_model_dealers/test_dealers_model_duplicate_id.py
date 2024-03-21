import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealers_model_duplicate_id(test_dealer_instance):
    """
    Test to ensure that creating a Dealers object with a duplicate D_ID
    raises a ValidationError due to the unique constraint on the D_ID field.
    """
    initial_dealer = test_dealer_instance

    # Attempt to create another dealer with the same D_ID as the initial dealer
    with pytest.raises(ValidationError) as excinfo:
        duplicate_dealer = Dealers(
            D_ID=initial_dealer.D_ID,  # Attempt to use the same D_ID
            DealerName="Second Dealer",
            DealerVATnumber="643999108",
            DealerEmail="seconddealer@example.com",
        )
        duplicate_dealer.full_clean()  # This should trigger the ValidationError

    # Optional: If you want to assert something about the exception message
    assert 'D_ID' in excinfo.value.message_dict, "D_ID field error not raised"
    assert 'already exists' in str(excinfo.value), "Expected unique constraint error message not found"