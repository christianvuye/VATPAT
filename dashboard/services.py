from .models import (
    CreditNotes, 
    CreditNoteResume,
    AcknowledgementRequest
)
from .utils import get_previous_month_date_range
from .email_templates import credit_note_email_template
from datetime import datetime
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.db.models import Count, Sum
from django.db.models.query import QuerySet

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

def generate_email_content(dealer, credit_notes, template):
    """
    Generate email content based on template, dealer, and credit notes.
    """
    recipient = dealer
    
    subject = template.get('subject')
    body = template.get('body')
    table_header = template.get('table_header')
    table_rows = template.get('table_rows')
    table_footer = template.get('table_footer')
    signature = template.get('signature')

    for note in credit_notes:
        issued_date = note.IssuedDate.strftime('%d-%m-%Y')
        total_vat_amount = f"{note.TotalVATAmountDocumentt:.2f}"
        table_rows += format_html(
            """
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            """,
            note.CN_ID,
            issued_date,
            total_vat_amount
        )
    
    e_mail_content = format_html(
        """
        <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <p>Assunto: {}</p>
            <p>Prezado(a) {}</p>
            {}
            {}
            {}
            {}
            {}
        </body>
        </html>
        """,
        mark_safe(subject),
        mark_safe(recipient),
        mark_safe(body),
        mark_safe(table_header),
        mark_safe(table_rows),
        mark_safe(table_footer),
        mark_safe(signature)
    )

    return e_mail_content

"""
Waiting on input from Jessamyn on what the best approach for this is.

Should the email content be saved to a file at all or should it added to the CreditNoteResumeEmail model as a field?

@Jessamyn: Could you provide guidance on this? What would be the best approach to handle this?
"""
def save_email_content_to_file(email_content, dealer_name):
    """
    Save email content to a file.
    """
    current_month = datetime.now().strftime('%B')
    file_name = f'{dealer_name}_credit_note_resume_email_{current_month}.html'

    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(email_content)
    print(f'Saved email content to file: {file_name}')

"""
@Jessamyn: Could you provide guidance on what the best approach for sending emails with Django is?

We are using Azure, could you provide me with some guidance on how to set up email sending with Azure?
"""
def send_acknowledgement_request_email(acknowledgement_request, dealer_instance, template): # pass the generated email content as an argument somehow
    """
    Send an acknowledgement request email to a dealer.
    """
    subject = template.get('subject')
    body = template.get('body')
    from_email = "hp.finance@honda-eu.com"
    to_email = dealer_instance.DealerEmail

    send_mail(
        subject,
        body,
        from_email,
        [to_email],
        fail_silently=False
    )
    print(f'Sent acknowledgement request email to: {to_email}')

    #increment_reminders_sent