import pytest
from django.utils import timezone
from dashboard.models import Dealers, CreditNotes

@pytest.fixture
def create_dealer():
    now = timezone.now()
    return Dealers.objects.create(
        D_ID='D001',
        DealerName='Test Dealer',
        DealerVATnumber='123456789',
        DealerEmail='test@example.com',
        CreatedDate=now,
        ModifiedDate=now
    )

@pytest.mark.django_db
def test_credit_note_foreign_key_to_dealer(create_dealer):
    dealer = create_dealer

    with pytest.raises(AttributeError):
        credit_note = CreditNotes.objects.create(
            CN_ID='CN001',
            D_ID=dealer,  # This line is expected to raise AttributeError
            TotalDocumentAmount=12345.67,
            TotalVATAmountDocumentt=1234.56,
            TotalDocumentAmountWithVAT=13580.23,
            AccountingNumberID='AN12345',
            IssuedDate=timezone.now()
        )
