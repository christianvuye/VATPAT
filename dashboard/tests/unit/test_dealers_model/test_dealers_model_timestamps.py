import pytest

@pytest.mark.django_db
def test_dealers_model_timestamps(test_dealer_instance_no_timestamps):
    """
    Test that `CreatedDate` and `ModifiedDate` fields in the Dealers model
    are set upon instance creation.
    """
    dealer = test_dealer_instance_no_timestamps
    
    assert dealer.CreatedDate is not None, "CreatedDate not set on new instance"
    assert dealer.ModifiedDate is not None, "ModifiedDate not set on new instance"
