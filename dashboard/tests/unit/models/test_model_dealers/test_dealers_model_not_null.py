import pytest
from django.db import transaction
from django.db.utils import IntegrityError
from dashboard.models import Dealers

@pytest.mark.django_db
def test_dealers_model_not_null(test_dealer_data_all_null):
    with transaction.atomic():    
        with pytest.raises(IntegrityError):
            Dealers.objects.create(**test_dealer_data_all_null)