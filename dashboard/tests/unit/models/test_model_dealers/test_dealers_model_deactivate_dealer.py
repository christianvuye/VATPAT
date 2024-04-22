import pytest
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealers_model_deactivate_dealer(test_dealer_data):
    """Test that deactivating a dealer does not affect other dealer data."""
    # Create a dealer using the fixture data
    dealer = Dealers.objects.create(**test_dealer_data)

    # Save initial data for comparison
    initial_data = {
        "D_ID": dealer.D_ID,
        "DealerName": dealer.DealerName,
        "DealerVATnumber": dealer.DealerVATnumber,
        "DealerEmail": dealer.DealerEmail,
        "is_active": dealer.is_active
    }

    # Explicitly set is_active to False
    dealer.is_active = False
    dealer.save()

    # Fetch the updated dealer and verify other fields are unchanged
    updated_dealer = Dealers.objects.get(D_ID=dealer.D_ID)
    assert updated_dealer.DealerName == initial_data["DealerName"]
    assert updated_dealer.DealerVATnumber == initial_data["DealerVATnumber"]
    assert updated_dealer.DealerEmail == initial_data["DealerEmail"]
    assert updated_dealer.is_active == False  # Check if is_active has been updated to False