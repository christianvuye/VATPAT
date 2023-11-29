import pytest
from django.utils import timezone
from dashboard.models import AcknowledgementRequest

@pytest.fixture
def create_acknowledgement_request():
    now = timezone.now()  # timezone-aware datetime
    return AcknowledgementRequest.objects.create(
        CNR_ID=1,  # Assuming a valid CNR_ID, change as necessary
        Status=True,
        CreatedDate=now,
        SendDate=now
    )

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_acknowledgement_request(create_acknowledgement_request):
    all_ack_requests = AcknowledgementRequest.objects.all()

    # Ensure we can fetch AcknowledgementRequest objects, indicating no basic mismatch
    assert all_ack_requests.exists(), "Failed to fetch AcknowledgementRequest objects from the database."
    assert create_acknowledgement_request in all_ack_requests, "Created AcknowledgementRequest object is not in the database."
