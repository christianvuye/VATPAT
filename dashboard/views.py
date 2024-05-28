from django.shortcuts import render
from .services import (
    collect_credit_notes_from_previous_month,
    collect_unique_dealers_from_credit_notes, 
    credit_notes_previous_month_per_dealer_dict,
    create_credit_note_resume_emails,
    credit_notes_totals_per_dealer
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

def dashboard_2_view(request):
    credit_notes = collect_credit_notes_from_previous_month()

    unique_dealers = collect_unique_dealers_from_credit_notes(credit_notes)

    grouped_credit_notes = credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealers)

    totals_per_dealer = credit_notes_totals_per_dealer(grouped_credit_notes)

    return render(request, 'dashboard/dashboard_2.html', {
        'unique_dealers': unique_dealers,
        'grouped_credit_notes': grouped_credit_notes,
        'totals_per_dealer': totals_per_dealer
    })