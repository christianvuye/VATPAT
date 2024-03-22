import pytest
from django.core.exceptions import ValidationError
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealers_model_not_null(test_dealer_data_all_null):
    with pytest.raises(ValidationError):
        dealer = Dealers(**test_dealer_data_all_null)
        dealer.full_clean()  # This triggers the model validation
