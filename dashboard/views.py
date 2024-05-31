from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .services import (
    collect_credit_notes_from_previous_month,
    collect_unique_dealers_from_credit_notes, 
    credit_notes_previous_month_per_dealer_dict,
    credit_notes_totals_per_dealer
)

class CustomLoginView(LoginView):
    """
    Custom login view that uses the login.html template.
    """
    template_name = 'login.html'

# Django recommends using function-based views over class-based views when the view is simple.
# In this case, the view is simple and does not require any additional methods or attributes.
# Therefore, we use a function-based view. 
# But check with Jessamyn what she thinks is the right approach.

#@login_required
def dashboard_view(request):
    """
    Renders the dashboard view with the data from the previous month.
    """
    credit_notes = collect_credit_notes_from_previous_month()

    unique_dealers = collect_unique_dealers_from_credit_notes(credit_notes)

    grouped_credit_notes = credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealers)

    totals_per_dealer = credit_notes_totals_per_dealer(grouped_credit_notes)

    return render(request, 'dashboard/dashboard.html', {
        'unique_dealers': unique_dealers,
        'grouped_credit_notes': grouped_credit_notes,
        'totals_per_dealer': totals_per_dealer
    })