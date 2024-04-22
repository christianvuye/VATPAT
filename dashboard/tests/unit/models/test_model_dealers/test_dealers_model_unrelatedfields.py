import pytest
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealers_model_unrelatedfields(test_dealer_data):
    """
    Test that updating specific fields of a Dealer does not inadvertently change other fields.
    """

    # Create the dealer using the fixture data
    test_dealer = Dealers.objects.create(**test_dealer_data)

    # Record original values of all fields
    original_name = test_dealer.DealerName
    original_vat = test_dealer.DealerVATnumber
    original_email = test_dealer.DealerEmail
    original_created_date = test_dealer.CreatedDate

    # Update the DealerName
    new_name = "New Dealer Name"
    test_dealer.DealerName = new_name
    test_dealer.save()

    # Refresh the instance from the database
    test_dealer.refresh_from_db()

    # Assert that only DealerName has changed and to the correct new value
    assert test_dealer.DealerName == new_name, "DealerName should be updated to the new value."
    assert test_dealer.DealerName != original_name, "DealerName should have changed from the original."

    # Assert that other fields remain unchanged
    assert test_dealer.DealerVATnumber == original_vat, "DealerVATnumber should not change."
    assert test_dealer.DealerEmail == original_email, "DealerEmail should not change."
    assert test_dealer.CreatedDate == original_created_date, "CreatedDate should not change."
    assert test_dealer.is_active == True, "is_active should not change."