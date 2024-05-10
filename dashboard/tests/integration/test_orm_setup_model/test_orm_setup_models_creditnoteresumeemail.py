import pytest
from django.utils import timezone
from dashboard.models import CreditNoteResumeEmail, CreditNotes, Dealers
from decimal import Decimal


@pytest.fixture
def create_credit_note_resume_email():

    # Create a dummy Dealer instance
    dealer = Dealers.objects.create(
        D_ID="PT123456",
        DealerName="Dummy Dealer",
        DealerVATnumber="538046554",
        DealerEmail="dummydealer@example.com",
        CreatedDate=timezone.now(),
        ModifiedDate=timezone.now()
    )

    # Create a dummy CreditNote instance
    credit_note = CreditNotes.objects.create(
        CN_ID="CN001",
        D_ID=dealer,  # Reference the dummy dealer instance
        TotalDocumentAmount=Decimal('12345.67'),
        TotalVATAmountDocumentt=Decimal('1234.56'),
        TotalDocumentAmountWithVAT=Decimal('13580.23'),
        AccountingNumberID="AN12345",
        IssuedDate=timezone.now()
    )

    now = timezone.now()  # timezone-aware datetime for the DateIssued
    return CreditNoteResumeEmail.objects.create(
        CN_ID=credit_note,
        DateIssued=timezone.now(),
        Month=timezone.now().month,
        Year=timezone.now().year,
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