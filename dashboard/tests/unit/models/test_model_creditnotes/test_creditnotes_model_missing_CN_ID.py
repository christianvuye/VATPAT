import pytest
from django.db import IntegrityError
from dashboard.models import CreditNotes, Dealers

@pytest.mark.django_db
def test_creditnotes_model_missing_CN_ID(test_credit_note_data_missing_cn_id, test_dealer_data):
    """Test CreditNotes model with missing CN_ID."""
    dealer = Dealers.objects.create(**test_dealer_data)
    with pytest.raises(IntegrityError):
        CreditNotes.objects.create(D_ID=dealer, **test_credit_note_data_missing_cn_id)