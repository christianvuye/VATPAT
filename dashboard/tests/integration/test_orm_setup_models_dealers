import pytest
from dashboard.models import Dealers

@pytest.mark.django_db
def test_orm_setup_for_dealers():
    all_dealers = Dealers.objects.all()

    # Ensure we can fetch dealers, indicating no basic mismatch
    assert all_dealers.exists(), "Failed to fetch dealers from the database."
