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

"""
This looks like shit. It needs to be fixed, but the models need to be set up correctly for this. 

Add type hints to the functions and make them more generic. Avoid hardcoding model names and field names in the functions.

Make functions more pure by removing print statements and side effects. Instead, return the data and let the caller decide what to do with it.

Avoid using global variables in functions. Pass the required data as arguments to the functions.

Avoid HTML formatting in Python code. Instead, use templates to generate HTML content.

Create a function that gets credit notes or credit note resume emails for a specific date or date range. 

This could be two separate functions, one for credit notes and one for credit note resume emails. -> get_credit_notes_by date(date) and get_credit_note_resume_emails_by_date(date)
"""

"""
This function should be more generic and get credit notes by date.

def get_credit_notes_by_date(start_date: datetime, end_date: datetime) -> QuerySet: 
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])

    return credit_notes

Evaluation criteria for change:
1. Necessity: Not essential for core functionality, as the existing function works. However, it would be beneficial to make the function more generic to reuse it for other date ranges.
2. Impact: The change does not break existing functionality but requires modifications to the function.
3. Complexity: The change reduces complexity by making the function more generic and reusable.
4. Performance: The change does not improve performance.
5. User Experience: The change does not directly impact user experience. 
6. Testing: The change can be thoroughly tested and validated within the available time.
7. Maintainability: The change improves maintainability by making the function more generic, reusable, and easier to read. 

Conclusion: The change is recommended as it improves the code quality and maintainability without significant drawbacks.
"""

"""
Consider whether this function is needed or if the QuerySet filter can be done directly in another function.

It is only used in one place, so it might be more straightforward to do the filter directly in that function.

Arguably, this function adds an unnecessary layer of abstraction and complexity as objects.filter is clear and concise.

Conclusion: This function can be removed to simplify the code and reduce unnecessary complexity.
"""
def collect_credit_notes_from_previous_month():
    """
    Collect all credit notes from the previous month.
    """
    start_date, end_date = get_previous_month_date_range() 
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])
    
    return credit_notes

"""
Does this function need to exist? Can the unique dealers from a given QuerySet be filtered with a query directly?

This function is only used in one place, so it might be more straightforward to do the filtering directly in that function.

Instead of using Python code to filter unique dealers, use a query directly in the database. This will improve performance and reduce complexity.

1. Necessity: Not essential for core functionality, as the existing function works.
2. Impact: The change does not break existing functionality but requires modifications of a different function.
3. Complexity: The change reduces complexity by removing an unnecessary function.
4. Performance: The change improves performance by using a database query instead of filtering in Python.
5. User Experience: The change improves performance, which can enhance user experience.
6. Testing: The change can be thoroughly tested and validated within the available time.
7. Maintainability: The change improves maintainability by simplifying the code and reducing unnecessary complexity.

Conclusion: The change is recommended as it improves performance and maintainability without significant drawbacks.
"""
def collect_unique_dealers_from_credit_notes(credit_notes):
    """
    Collect all unique dealers from a credit_notes queryset.
    """
    unique_dealer_list = []

    for note in credit_notes: 
        if note.D_ID.DealerName not in unique_dealer_list:
            unique_dealer_list.append(note.D_ID.DealerName)
    
    return unique_dealer_list

"""
Question the necessity of this function. Can the grouping and aggregation be done directly with a query the database?
"""
def credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealer_list):
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

"""
Question the necessity of this function. Can the aggregation and annotation be done directly with a query in the database instead of using Python code?

Should these totals be added to the CreditNotesResumeEmail model as fields? 

@Jessamyn: Could you give your input on this and what would be the best approach to handle this?

I believe you could do the entire thing as a single queryset. See notes in view.

"""
def credit_notes_totals_per_dealer(grouped_credit_notes):
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

"""
Waiting for input from Jessamyn on what the best approach for this is. 

Should the email content be generated in the service layer or should it be generated in the view layer?

Should the email content be generated in the view layer and passed to the service layer for sending?

@Jessamyn: Could you provide guidance on this? What would be the best approach to handle this?

@hen it comes to sending email, I usually make a small helper function, like this: https://github.com/jessamynsmith/eggtimer-server/blob/master/periods/email_sender.py
Then I have email templates as files, and use the django get_template and render functions to populate the template with context, e.g. https://github.com/jessamynsmith/eggtimer-server/blob/master/periods/management/commands/notify_upcoming_period.py#L60
As you can see here, I have a bunch of different templates, with both a text and html version, that all inherit from the base template (that contains styles and signature)
https://github.com/jessamynsmith/eggtimer-server/tree/master/periods/templates/periods/email
I don't have strong feelings about whether you call the email code in the view or the service, though it feels more like a service layer thing.
(note that if you do what I'm suggesting, you won't have to generate html in python and mark_safe)
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
-> I typically save email content as a TextField in the database rather than a file, though it depends on your
server setup and needs. I like the database because it's easily searchable even if you don't have access to the
server filesystem.
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
This is useful if you need to know what fields are available on an object. In particular, it will show you
the reverse foreign key relationships generated by Django. e.g.
dealers = Dealers.objects.all()
print(dir(dealers[0]))
I expect you'll see a field like "creditnotes_set" which represents all credit notes connected to that dealer.
If you don't supply a related_name on a foreign key, Django generates a name for the reverse relationship which is
normally the name of the model that has the foreign key, lowercased, plus '_set'

A function should do one thing, so split this function into smaller functions later when refactoring and pass the required data as arguments.

#dealer.creditnotes_set.all() -> This is a query that fetches all credit notes for a specific dealer. It is not clear why this is mentioned here. Could you provide more context?
I was just making sure that you understood that in Django, all foreign keys can be referenced from either side
(the model that has the foreign key, and the model that is linked to). This is a somewhat unusual and very useful
feature of Django.

@Jessamyn: I feel that creating Credit Note Resumes this way is not the best approach. Could you provide guidance on what you think is the most logical way to create Credit Note Resumes?
"""

def create_credit_note_resume_emails(): 
    """
    Create CreditNoteResumeEmail instances for each unique dealer based on the credit notes from the previous month.
    """
    credit_notes = collect_credit_notes_from_previous_month() 
    
    unique_dealers = collect_unique_dealers_from_credit_notes(credit_notes)
    
    grouped_credit_notes = credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealers)
    
    # As mentioned elsewhere, I think you could collect the necessary data in a single queryset.
    # I initiall expected emails to be sent in this loop as well, but I guess that happens elsewhere.
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
        
        # If notes is a queryset, you can update all of them with one query:
        # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.update
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
Other than the one small note below, seems fine.
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
            # I believe that providing CreatedDate here will do nothing, since the model has auto_now_add
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
I agree, I would keep all the related functionality together, and increment when you send.
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
See my extensive comments above on email

We are using Azure, could you provide me with some guidance on how to set up email sending with Azure?
I have not used Azure specifically. This package might be helpful:
https://pypi.org/project/django-azure-communication-email/
In general, if your email provider allows SMTP (does Azure? I don't know), you can set that up easily in Django:
https://docs.djangoproject.com/en/5.0/topics/email/
"""
def send_acknowledgement_request_email(acknowledgement_request, dealer_instance, template): # pass the generated email content as an argument somehow
    """
    Send an acknowledgement request email to a dealer.
    """
    subject = template.get('subject')
    body = template.get('body')
    # I strongly recommend having from_email as an environment variable that is loaded in settings.
    from_email = "hp.finance@honda-eu.com"
    to_email = dealer_instance.DealerEmail

    # 
    send_mail(
        subject,
        body,
        from_email,
        [to_email],
        fail_silently=False
    )
    print(f'Sent acknowledgement request email to: {to_email}')

    increment_reminders_sent(acknowledgement_request)