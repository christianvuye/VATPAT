from .models import (
    CreditNotes, 
    CreditNoteResume,
    AcknowledgementRequest,
    Dealers
)
from .utils import get_previous_month_date_range
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count, Sum
from django.db.models.query import QuerySet
from django.conf import settings
from email.utils import formataddr

def create_credit_note_resume() -> None: 
    """
    Create CreditNoteResume instances for each unique dealer based on the credit notes from the previous month.
    """
    # Get the date range for the previous month
    start_date, end_date = get_previous_month_date_range()

    # Get all credit notes issued in the previous month
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])

    # Group and aggregate the credit notes by dealer
    grouped_credit_notes = credit_notes.values('D_ID').annotate(
        total_credit_notes=Count('CN_ID'),
        total_document_amount=Sum('TotalDocumentAmount'),
        total_vat_amount=Sum('TotalVATAmountDocumentt'),
        total_document_amount_with_vat=Sum('TotalDocumentAmountWithVAT')
    )

    # Create a CreditNoteResume instance for each unique dealer
    for item in grouped_credit_notes:
        # Create a CreditNoteResume instance
        credit_note_resume = CreditNoteResume.objects.create(
            TotalCreditNotes=item['total_credit_notes'],
            TotalDocumentAmounts=item['total_document_amount'],
            TotalVATAmounts=item['total_vat_amount'],
            TotalDocumentAmountsWithVAT=item['total_document_amount_with_vat']
        )

        # Update the credit notes with the CreditNoteResume ID
        CreditNotes.objects.filter(
            IssuedDate__range=[start_date, end_date],
            D_ID=item['D_ID']
        ).update(CNR_ID=credit_note_resume)

def create_acknowledgement_request(credit_note_resumes: QuerySet) -> None:
    """
    Create AcknowledgementRequest instances from a set of CreditNoteResume records.
    """
    for resume in credit_note_resumes:
        acknowledgement_request = AcknowledgementRequest.objects.create(
            CNR_ID=resume,
            SendDate=datetime.now(), # do not set this here, set it when sending the email
            RemindersSent=0
        )
        print(f'Created AcknowledgementRequest: {acknowledgement_request} for CreditNoteResumeEmail: {resume.CNR_ID}')

def send_acknowledgement_email(recipient: Dealers, subject: str, text_body: str, html_body: str) -> bool:
    """
    Send an acknowledgement email to a dealer.
    """
    recipients = [formataddr((recipient.DealerName, recipient.DealerEmail))]
    msg = EmailMultiAlternatives(
        subject, 
        text_body, 
        to=recipients,
        reply_to=settings.REPLY_TO
        )
    
    if html_body:
        msg.attach_alternative(html_body, "text/html")
    msg.send()
    return True