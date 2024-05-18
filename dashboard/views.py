from django.shortcuts import render
from .services import collect_credit_notes_from_previous_month

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def credit_notes_previous_month_view(request):
    credit_notes = collect_credit_notes_from_previous_month()
    return render(request, 'dashboard/credit_notes_previous_month.html', {'credit_notes': credit_notes})