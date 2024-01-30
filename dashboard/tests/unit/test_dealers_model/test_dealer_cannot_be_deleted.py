import pytest
from django.db import IntegrityError, OperationalError, DatabaseError

@pytest.mark.django_db
def test_dealer_cannot_be_deleted(test_dealer_instance):
    dealer = test_dealer_instance

    # Attempt to delete the dealer and expect an error
    with pytest.raises((IntegrityError, OperationalError, DatabaseError)):
        dealer.delete()