import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealers_model_email_validation(test_dealer_data):
    """
    Test to ensure that creating a Dealers object with an invalid email format
    in the DealerEmail field raises a ValidationError.
    """
    # Modify the test_dealer_data dict to use an invalid email format
    test_dealer_data["DealerEmail"] = "invalidemail"  # No '@' symbol, so it's invalid

    # Attempt to create a dealer with the invalid email format
    with pytest.raises(ValidationError) as excinfo:
        invalid_email_dealer = Dealers(**test_dealer_data)
        invalid_email_dealer.full_clean()  # This should trigger the ValidationError for the email

    # Optional: Assert something about the exception message
    assert 'DealerEmail' in excinfo.value.message_dict, "DealerEmail field error not raised"
    assert 'Enter a valid email address.' in str(excinfo.value), "Expected email format error message not found"
