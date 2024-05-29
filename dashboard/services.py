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

"""
Add type hints to the functions and make them more generic. Avoid hardcoding model names and field names in the functions.

Make functions more pure by removing print statements and side effects. Instead, return the data and let the caller decide what to do with it.

Avoid using global variables in functions. Pass the required data as arguments to the functions.

Avoid HTML formatting in Python code. Instead, use templates to generate HTML content.

Create a function that gets credit notes or credit note resume emails for a specific date or date range. 

This could be two separate functions, one for credit notes and one for credit note resume emails. -> get_credit_notes_by date(date) and get_credit_note_resume_emails_by_date(date)
"""

def collect_credit_notes_from_previous_month(): # make this function more generic, so it can take any range of dates
    """
    Collect all credit notes from the previous month.
    """
    start_date, end_date = get_previous_month_date_range()
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])
    
    return credit_notes # returns a QuerySet

def collect_unique_dealers_from_credit_notes(credit_notes): # make this function more generic, so it can collect unique value from a QuerySet of any model, params: QuerySet, field_name -> for example: collect_unique_values_queryset(credit_notes, 'D_ID.DealerName')
    """
    Collect all unique dealers from a credit_notes queryset.
    """

    unique_dealer_list = []

    for note in credit_notes: 
        if note.D_ID.DealerName not in unique_dealer_list:
            unique_dealer_list.append(note.D_ID.DealerName)
    
    return unique_dealer_list

def credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealer_list): # make this function more generic, so it can take any QuerySet and any list of unique values in that QuerySet
    """
    Create a dictionary with dealers as keys and their credit notes as values.
    """

    grouped_credit_notes = {}

    for dealer in unique_dealer_list:
        grouped_credit_notes[dealer] = []
        for note in credit_notes:
            if note.D_ID.DealerName == dealer:
                grouped_credit_notes[dealer].append(note)
    
    return grouped_credit_notes

def credit_notes_totals_per_dealer(grouped_credit_notes): # make this function more generic, so it can take any dictionary and calculate totals for any summable field in the values of the dictionary
    """
    Calculate the Total Document Amount, Total Document VAT Amount, and Total Document Amount with VAT for each dealer. 
    """

    totals_per_dealer = {}

    for dealer, notes in grouped_credit_notes.items():
        total_document_amount = 0
        total_document_vat_amount = 0
        total_document_amount_with_vat = 0

        for note in notes:
            total_document_amount += note.TotalDocumentAmount
            total_document_vat_amount += note.TotalVATAmountDocumentt
            total_document_amount_with_vat += note.TotalDocumentAmountWithVAT
        
        totals_per_dealer[dealer] = {
            'TotalDocumentAmount': total_document_amount,
            'TotalVATAmountDocumentt': total_document_vat_amount,
            'TotalDocumentAmountWithVAT': total_document_amount_with_vat
        }
    
    return totals_per_dealer

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

def save_email_content_to_file(email_content, dealer_name):
    """
    Save email content to a file.
    """
    current_month = datetime.now().strftime('%B')
    file_name = f'{dealer_name}_credit_note_resume_email_{current_month}.html'

    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(email_content)
    print(f'Saved email content to file: {file_name}')

def create_credit_note_resume_emails(): # a function should do one thing, so split this function into smaller functions later when refactoring
    """
    Create CreditNoteResumeEmail instances for each unique dealer based on the credit notes from the previous month.
    """
    credit_notes = collect_credit_notes_from_previous_month()
    
    unique_dealers = collect_unique_dealers_from_credit_notes(credit_notes)
    
    grouped_credit_notes = credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealers)
    
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

def get_credit_note_resume_emails_by_month_and_year(month, year):
    """
    Get CreditNoteResumeEmail instances for a specific month and year.
    """
    resume_emails = CreditNoteResumeEmail.objects.filter(Month=month, Year=year)
    
    return resume_emails # returns a QuerySet

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
            SendDate=datetime.now(),
            RemindersSent=0
        )
        print(f'Created AcknowledgementRequest: {acknowledgement_request} for CreditNoteResumeEmail: {resume.CNR_ID}')