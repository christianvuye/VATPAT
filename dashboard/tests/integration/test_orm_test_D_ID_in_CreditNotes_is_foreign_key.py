import pytest
from django.db import models
from dashboard.models import CreditNotes

@pytest.mark.django_db
def test_D_ID_in_CreditNotes_is_foreign_key():
    D_ID_field = CreditNotes._meta.get_field('D_ID')
    assert isinstance(D_ID_field, models.ForeignKey), "D_ID in CreditNotes is not a ForeignKey"