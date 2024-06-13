from django.shortcuts import render, redirect
from .models import Dealers, CreditNotes
from .utils import get_previous_months, get_previous_month_date_range
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.conf import settings
from decouple import config
import requests
import json

__version__ = "0.3.0"

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
    # Get the date range for the previous month
    start_date, end_date = get_previous_month_date_range()

    # Get all credit notes issued in the previous month
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])

    # Get the unique dealers
    dealers = credit_notes.values('D_ID', 'D_ID__DealerName').distinct() 

    # Group and aggregate the credit notes by dealer
    credit_notes_aggregated = credit_notes.values('D_ID').annotate(
        total_credit_notes=Count('CN_ID'),
        total_document_amount=Sum('TotalDocumentAmount'),
        total_vat_amount=Sum('TotalVATAmountDocumentt'),
        total_document_amount_with_vat=Sum('TotalDocumentAmountWithVAT')
    )

    return render(request, 'dashboard/dashboard.html', {
        'credit_notes': credit_notes,
        'dealers': dealers,
        'credit_notes_aggregated': credit_notes_aggregated
    }
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

#templates from identity django web app library
@settings.AUTH.login_required
def index(request):
    user = settings.AUTH.get_user(request)
    assert user  # User would not be None since we decorated this view with @login_required
    return render(request, 'index.html', dict(
        user=user,
        version=__version__,
        edit_profile_url=settings.AUTH.get_edit_profile_url(request),
        downstream_api=config('ENDPOINT'),
    ))

# Instead of using the login_required decorator,
# here we demonstrate how to handle the error explicitly.
def call_downstream_api(request):
    token = settings.AUTH.get_token_for_user(request, ('https://graph.microsoft.com/.default', "").split())
    if "error" in token:
        return redirect(settings.AUTH.login)
    api_result = requests.get(  # Use access token to call downstream api
        config('ENDPOINT'),
        headers={'Authorization': 'Bearer ' + token['access_token']},
        timeout=30,
    ).json()  # Here we assume the response format is json
    return render(request, 'display.html', {
        "title": "Result of downstream API call",
        "content": json.dumps(api_result, indent=4),
    })