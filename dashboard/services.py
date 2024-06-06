from .models import (
    CreditNotes, 
    CreditNoteResumeEmail,
    AcknowledgementRequest
)
from .utils import get_previous_month_date_range
from .email_templates import credit_note_email_template
from datetime import datetime
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.db.models import Count, Sum

"""
Waiting for input from Jessamyn on what the best approach for this is. 

Should the email content be generated in the service layer or should it be generated in the view layer?

Should the email content be generated in the view layer and passed to the service layer for sending?

@Jessamyn: Could you provide guidance on this? What would be the best approach to handle this?
"""
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
Waiting on input from Jessamyn on what the best approach for this is.

I have made several notes for Jessamyn to provide input on.

#print(dir(Objects)) -> Model.set -> I don't understand what this comment means. Could you provide more context?

A function should do one thing, so split this function into smaller functions later when refactoring and pass the required data as arguments.

#dealer.creditnotes_set.all() -> This is a query that fetches all credit notes for a specific dealer. It is not clear why this is mentioned here. Could you provide more context?

@Jessamyn: I feel that creating Credit Note Resumes this way is not the best approach. Could you provide guidance on what you think is the most logical way to create Credit Note Resumes?
"""

def create_credit_note_resume_emails(): 
    """
    Create CreditNoteResumeEmail instances for each unique dealer based on the credit notes from the previous month.
    """
    # Get the date range for the previous month
    start_date, end_date = get_previous_month_date_range()

    # Get all credit notes issued in the previous month
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])

    # Get a list of unique dealers from the credit notes for the previous month
    unique_dealers = credit_notes.values('D_ID').distinct()

    # Group and aggregate the credit notes by dealer
    grouped_credit_notes = credit_notes.values('D_ID').annotate(
        total_credit_notes=Count('CN_ID'),
        total_document_amount=Sum('TotalDocumentAmount'),
        total_vat_amount=Sum('TotalVATAmountDocumentt'),
        total_document_amount_with_vat=Sum('TotalDocumentAmountWithVAT')
    )
    
    now = datetime.now()
    month = now.month
    year = now.year

    for dealer_name, notes in grouped_credit_notes.items():
        resume_email = CreditNoteResumeEmail.objects.create(
            DateIssued=now,
            Month=month,
            Year=year
        )
        print(f'Created CreditNoteResumeEmail: {resume_email} for Dealer: {dealer_name}')

        email_content = generate_email_content(dealer_name, notes, credit_note_email_template)
        print(email_content)

        save_email_content_to_file(email_content, dealer_name)
        
        for note in notes:
            note.CNR_ID = resume_email
            note.save()
            print(f'Updated CreditNote: {note.CN_ID} with CreditNoteResumeEmail: {resume_email}')
"""
This function is not needed. It's simply doing a query that can be done directly somewhere else. 

Remove this function to simplify the code and reduce unnecessary complexity.
"""
def get_credit_note_resume_emails_by_month_and_year(month, year):
    """
    Get CreditNoteResumeEmail instances for a specific month and year.
    """
    resume_emails = CreditNoteResumeEmail.objects.filter(Month=month, Year=year)
    
    return resume_emails

"""
This function seems fine to me. It takes a queryset of CreditNoteResumeEmail instances and creates AcknowledgementRequest instances for each of them.

It would be good to add type hints to the function arguments and return types for clarity.

@Jessamyn: Could you provide guidance on whether this function is fine as it is or if there are any improvements that could be made?
"""
def create_acknowledgement_requests(credit_note_resumes):
    """
    Create AcknowledgementRequest instances from a set of CreditNoteResumeEmail records.

    Args:
        credit_note_resumes (QuerySet): A queryset or list of CreditNoteResumeEmail records.
    """
    for resume in credit_note_resumes:
        acknowledgement_request = AcknowledgementRequest.objects.create(
            CNR_ID=resume,
            CreatedDate=datetime.now(),
            SendDate=datetime.now(), # do not set this here, set it when sending the email
            RemindersSent=0
        )
        print(f'Created AcknowledgementRequest: {acknowledgement_request} for CreditNoteResumeEmail: {resume.CNR_ID}')

"""
Is this function really needed? 

It only does: acknowledgement_request.RemindersSent += 1 and acknowledgement_request.save().

This could be done directly in the function that sends the email.

Consider removing this function to simplify the code and reduce unnecessary complexity.

@Jessamyn: Could you provide guidance on whether this function is needed or if it can be removed?
"""
def increment_reminders_sent(acknowledgement_request):
    """
    Increment the number of reminders sent for an AcknowledgementRequest instance.
    """
    acknowledgement_request.RemindersSent += 1
    acknowledgement_request.save()
    print(f'Updated AcknowledgementRequest: {acknowledgement_request} with RemindersSent: {acknowledgement_request.RemindersSent}')

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

    increment_reminders_sent(acknowledgement_request)