import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealer_valid_vat(test_dealer_data_valid_vat):
    """
    Given a dealer instance with a valid VAT number,
    When the instance is validated,
    Then no ValidationError should be raised.
    """
    # Manually create a Dealers instance using the fixture data
    dealer = Dealers(**test_dealer_data_valid_vat)
    try:
        dealer.full_clean()
    except ValidationError:
        pytest.fail("ValidationError raised for a valid VAT number unexpectedly.")

@pytest.mark.django_db
def test_dealer_invalid_vat(test_dealer_data_invalid_vat):
    """
    Given a dealer instance with an invalid VAT number,
    When the instance is validated,
    Then a ValidationError should be raised.
    """
    # Manually create a Dealers instance using the fixture data
    dealer = Dealers(**test_dealer_data_invalid_vat)
    with pytest.raises(ValidationError):
        dealer.full_clean()