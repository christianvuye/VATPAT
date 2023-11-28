import pytest
from dashboard.models import Dealers

# The @pytest.mark.django_db decorator enables this test to access the Django database.
# It wraps the test in a transaction (rolled back after test) and resets auto-increment sequences,
# ensuring test isolation and consistent primary key sequences for each test run.

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_dealers():
    all_dealers = Dealers.objects.all()

    # Ensure we can fetch dealers, indicating no basic mismatch
    assert all_dealers.exists(), "Failed to fetch dealers from the database."