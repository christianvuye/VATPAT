import pytest

@pytest.mark.django_db
def test_dealers_model_charfields_string(test_dealer_instance):
    """
    Verify that CharFields in Dealers model store string values correctly.
    """
    dealer = test_dealer_instance
    
    # Asserting CharFields correctly store string values
    assert dealer.D_ID == "D001", "D_ID does not store string correctly"
    assert dealer.DealerName == "Test Dealer", "DealerName does not store string correctly"
    assert dealer.DealerVATnumber == "VAT12345678", "DealerVATnumber does not store string correctly"
    assert dealer.DealerEmail == "dealer@example.com", "DealerEmail does not store string correctly"
    
    # Verifying data types are strings
    assert isinstance(dealer.D_ID, str), "D_ID type mismatch"
    assert isinstance(dealer.DealerName, str), "DealerName type mismatch"
    assert isinstance(dealer.DealerVATnumber, str), "DealerVATnumber type mismatch"
    assert isinstance(dealer.DealerEmail, str), "DealerEmail type mismatch"
