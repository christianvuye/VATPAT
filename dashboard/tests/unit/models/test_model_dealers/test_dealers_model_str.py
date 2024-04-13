import pytest
from dashboard.models import Dealers 

@pytest.mark.django_db
def test_dealers_model_str(test_dealer_data):
    """
    Test that the string representation of the Dealer model includes the dealer name,
    VAT number, email, and D_ID.
    """
    dealer = Dealers.objects.create(**test_dealer_data)

    expected_str = f"PT123456 | Test Dealer | 253512182 | dealer@example.com | PT123456"
    assert str(dealer) == expected_str