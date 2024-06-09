from django.shortcuts import render
from .models import Dealers
from .utils import get_previous_months
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

"""
Consider using class based views for everything.

With class based views, all views share a consistent structure and can be easily extended or customized.

DashboardView could be a ListView, with the model being CreditNotes and the grouping could be done in get_queryset.
"""

class CustomLoginView(LoginView):
    """
    Custom login view that uses the login.html template.
    """
    template_name = 'login.html'

@login_required
def dashboard_view(request):
    """
    Renders the dashboard view with the data from the previous month.
    """

    return render(request, 'dashboard/dashboard.html', 
                  )

@login_required
def dashboard_view_acknowledgements(request):
    """
    Renders a dashboard view with the acknowledgement tracking from the previous months.
    """
    dealers = Dealers.objects.all()

    # Get the current and previous 3 months
    months = get_previous_months(4)

    return render(request, 'dashboard/dashboard_acknowledgements.html', {
        'dealers': dealers,
        'months': months
    })