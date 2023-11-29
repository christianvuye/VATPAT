import pytest
from dashboard.models import AcknowledgementReceived

@pytest.fixture
def create_acknowledgement_received():
    # Assuming a binary file-like object for MsgFile. You can adjust this as needed.
    msg_file_content = b"Sample binary content"
    return AcknowledgementReceived.objects.create(
        R_ID=1,  # Assuming a valid R_ID, change as necessary
        MsgFile=msg_file_content
    )

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_acknowledgement_received(create_acknowledgement_received):
    all_ack_received = AcknowledgementReceived.objects.all()

    # Ensure we can fetch AcknowledgementReceived objects, indicating no basic mismatch
    assert all_ack_received.exists(), "Failed to fetch AcknowledgementReceived objects from the database."
    assert create_acknowledgement_received in all_ack_received, "Created AcknowledgementReceived object is not in the database."
