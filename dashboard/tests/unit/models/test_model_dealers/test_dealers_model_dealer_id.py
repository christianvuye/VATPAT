import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealer_valid_d_id(test_dealer_data_valid_d_id):
    """
    Given a dealer instance with a valid D_ID,
    When the instance is validated,
    Then no ValidationError should be raised.
    """
    # Manually create a Dealers instance using the fixture data
    dealer = Dealers(**test_dealer_data_valid_d_id)
    try:
        dealer.full_clean()
    except ValidationError:
        pytest.fail("ValidationError raised for a valid D_ID unexpectedly.")

@pytest.mark.django_db
def test_dealer_invalid_d_id(test_dealer_data_invalid_d_id):
    """
    Given a dealer instance with an invalid D_ID,
    When the instance is validated,
    Then a ValidationError should be raised.
    """
    # Manually create a Dealers instance using the fixture data
    dealer = Dealers(**test_dealer_data_invalid_d_id)
    with pytest.raises(ValidationError):
        dealer.full_clean()
