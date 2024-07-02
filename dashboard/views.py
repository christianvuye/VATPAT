from django.shortcuts import render
from .models import Dealers, CreditNotes
from .utils import get_previous_months, get_previous_month_date_range
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum

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