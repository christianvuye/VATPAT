from django.shortcuts import render
from .services import (
    collect_credit_notes_from_previous_month,
    collect_unique_dealers_from_credit_notes, 
    credit_notes_previous_month_per_dealer_dict,
    create_credit_note_resume_emails
)

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def credit_notes_previous_month_view(request):
    credit_notes = collect_credit_notes_from_previous_month()
    return render(request, 'dashboard/credit_notes_previous_month.html', {'credit_notes': credit_notes})

def credit_notes_previous_month_grouped_by_dealer_view(request):
    credit_notes = collect_credit_notes_from_previous_month()
    unique_dealer_list = collect_unique_dealers_from_credit_notes(credit_notes)
    credit_notes_grouped = credit_notes_previous_month_per_dealer_dict(credit_notes, 
                                                                       unique_dealer_list
                                                                       )
    return render(request, 
                  'dashboard/credit_notes_previous_month_grouped_by_dealer.html', 
                  {'credit_notes': credit_notes_grouped}
                  )

def create_credit_note_resume_emails_view(request):
    create_credit_note_resume_emails()
    return render(request, 'dashboard/credit_note_resume_emails.html')