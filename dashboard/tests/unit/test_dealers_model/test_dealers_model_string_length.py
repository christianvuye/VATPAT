import pytest
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_dealers_model_string_length(test_dealer_instance):
    # Test D_ID field max_length
    with pytest.raises(ValidationError) as exc_info:
        test_dealer_instance.D_ID = 'x' * 11  # Exceeds max_length
        test_dealer_instance.full_clean()
    assert 'D_ID' in exc_info.value.error_dict, "D_ID max_length constraint not triggered"

    # Test DealerName field max_length
    with pytest.raises(ValidationError) as exc_info:
        test_dealer_instance.DealerName = 'x' * 101  # Exceeds max_length
        test_dealer_instance.full_clean()
    assert 'DealerName' in exc_info.value.error_dict, "DealerName max_length constraint not triggered"

    # Test DealerVATnumber field max_length
    with pytest.raises(ValidationError) as exc_info:
        test_dealer_instance.DealerVATnumber = 'x' * 21  # Exceeds max_length
        test_dealer_instance.full_clean()
    assert 'DealerVATnumber' in exc_info.value.error_dict, "DealerVATnumber max_length constraint not triggered"

    # Test DealerEmail field max_length
    with pytest.raises(ValidationError) as exc_info:
        test_dealer_instance.DealerEmail = 'x' * 81  # Exceeds max_length
        test_dealer_instance.full_clean()
    assert 'DealerEmail' in exc_info.value.error_dict, "DealerEmail max_length constraint not triggered"
