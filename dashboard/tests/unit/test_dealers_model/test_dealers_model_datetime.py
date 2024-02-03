import pytest
from datetime import datetime

@pytest.mark.django_db
def test_dealers_model_datetime(test_dealer_instance):
    """
    Ensure DateTimeFields in Dealers model store datetime objects correctly.
    """
    dealer = test_dealer_instance
    
    # Verify that datetime fields are set
    assert dealer.CreatedDate is not None, "CreatedDate is not set"
    assert dealer.ModifiedDate is not None, "ModifiedDate is not set"
    
    # Verify that datetime fields are instances of datetime.datetime
    assert isinstance(dealer.CreatedDate, datetime), "CreatedDate is not a datetime object"
    assert isinstance(dealer.ModifiedDate, datetime), "ModifiedDate is not a datetime object"