import pytest
from django.utils import timezone
from dashboard.models import CreditNoteResumeEmail

@pytest.fixture
def create_credit_note_resume_email():
    now = timezone.now()  # timezone-aware datetime for the DateIssued
    return CreditNoteResumeEmail.objects.create(
        CN_ID='CN001',
        DateIssued=now,
        Month=now.month,
        Year=now.year,
        Body='Test Body of the email',
        Subject='Test Subject',
        Status=True,
        IsValid=True
    )

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_orm_setup_for_credit_note_resume_email(create_credit_note_resume_email):
    all_cnr_emails = CreditNoteResumeEmail.objects.all()

    # Ensure we can fetch CreditNoteResumeEmail objects, indicating no basic mismatch
    assert all_cnr_emails.exists(), "Failed to fetch CreditNoteResumeEmail objects from the database."
    assert create_credit_note_resume_email in all_cnr_emails, "Created CreditNoteResumeEmail object is not in the database."
