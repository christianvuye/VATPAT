import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Dealers
from django.utils import timezone

@pytest.mark.django_db
def test_dealers_model_unique(test_dealer_instance):
    # Fixture 'create_initial_dealer' is used to create the first dealer instance
    initial_dealer = test_dealer_instance

    # Attempt to create another dealer with the same D_ID as the initial dealer
    with pytest.raises(ValidationError) as excinfo:
        Dealers.objects.create(
            D_ID=initial_dealer.D_ID,
            DealerName="Second Dealer",
            DealerVATnumber="246426993",
            DealerEmail="seconddealer@example.com",
            CreatedDate=timezone.now(),
            ModifiedDate=timezone.now(),
            is_active=True
        ).full_clean()
    
    # Check if the ValidationError message is what we expect
    assert 'D_ID' in excinfo.value.message_dict
    assert 'already exists' in excinfo.value.message_dict['D_ID'][0]