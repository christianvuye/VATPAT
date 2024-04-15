import pytest
from dashboard.models import Dealers
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_dealers_model_data_integrity(test_dealer_data):
    
    dealer = Dealers.objects.create(**test_dealer_data)
    """
    Test that updating a dealer instance maintains the integrity of the data.
    """
    
    #Update some data of the dealer instance
    dealer.DealerName = "Updated Dealer Name"
    dealer.DealerVATnumber = "241964644"
    dealer.DealerEmail = "updatedemail@example.com"

    #Validate the updated data against model constraints and Save the updated dealer instance
    try:
        dealer.full_clean()
        dealer.save()
    except ValidationError as e:
        pytest.fail(f"Dealer data integrity failed: {e}")

    #Re-fetch the dealer instance to ensure the data integrity is maintained"
    updated_dealer = Dealers.objects.get(D_ID=dealer.D_ID)
    assert updated_dealer.DealerName == "Updated Dealer Name"
    assert updated_dealer.DealerVATnumber == "241964644"
    assert updated_dealer.DealerEmail == "updatedemail@example.com"