import pytest
from django.utils import timezone
from django.core.exceptions import ValidationError
from dashboard.models import Dealers

@pytest.fixture
def dealer_instance():
    # Create a Dealer instance with predefined data
    dealer = Dealers.objects.create(
        D_ID="D001",
        DealerName="Test Dealer",
        DealerVATnumber="VAT12345678",
        DealerEmail="dealer@example.com",
        CreatedDate=timezone.now(),
        ModifiedDate=timezone.now()
    )
    return dealer


@pytest.mark.django_db
def test_dealers_model_string_max_length_constraints(dealer_instance):
    # Test D_ID field max_length
    with pytest.raises(ValidationError) as exc_info:
        dealer_instance.D_ID = 'x' * 11  # Exceeds max_length
        dealer_instance.full_clean()
    assert 'D_ID' in exc_info.value.error_dict, "D_ID max_length constraint not triggered"

    # Test DealerName field max_length
    with pytest.raises(ValidationError) as exc_info:
        dealer_instance.DealerName = 'x' * 101  # Exceeds max_length
        dealer_instance.full_clean()
    assert 'DealerName' in exc_info.value.error_dict, "DealerName max_length constraint not triggered"

    # Test DealerVATnumber field max_length
    with pytest.raises(ValidationError) as exc_info:
        dealer_instance.DealerVATnumber = 'x' * 21  # Exceeds max_length
        dealer_instance.full_clean()
    assert 'DealerVATnumber' in exc_info.value.error_dict, "DealerVATnumber max_length constraint not triggered"

    # Test DealerEmail field max_length
    with pytest.raises(ValidationError) as exc_info:
        dealer_instance.DealerEmail = 'x' * 81  # Exceeds max_length
        dealer_instance.full_clean()
    assert 'DealerEmail' in exc_info.value.error_dict, "DealerEmail max_length constraint not triggered"
