from django.shortcuts import render
from .models import Dealers
from .utils import get_previous_months
from django.contrib.auth.views import LoginView
#from django.contrib.auth.decorators import login_required
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
# Personally, I prefer to use class-based for everything -- I like the consistency of having all
# views share a structure, and most views correspond to one of the generic views.
# It can also make it easier if you need to add more to the view later.
# e.g. you could turn dashboard_view into ListView, with the model being CreditNotes, and the 
# grouping etc could be done in get_queryset.
# That said, there is nothing wrong with function-based views, and many people still use them.

# Note on templates: I STRONGLY recommend having a common base.html that all templates inherit from.
# This guarantees a consistent look and feel on your site, ensures you are using the same versions of
# JS libraries, and generally makes your life MUCH easier. I also recommend having your custom JS in .js
# files that are loaded into the template via static. This gives you options like linting the JS, 
# compressing it, loading it from a CDN, etc.
# Feel free to refer to my eggtimer project:
# https://github.com/jessamynsmith/eggtimer-server/blob/master/eggtimer/templates/base.html
# Note that the base template typically needs blocks to allow inheritors to enter their own title,
# head content, body content, and js/footer content.


# clean up all the code related to required login before being able to access the dashboard
#@login_required
def dashboard_view(request):
    """
    Renders the dashboard view with the data from the previous month.
    """
    credit_notes = collect_credit_notes_from_previous_month()

    # It should be possible to do away with all the small helper functions and generate the necessary
    # data with a single queryset, something like the following (note that I don't have your db set up so
    # this is not tested.
    # credit_nodes.values('D_ID__D_ID', 'D_ID__DealerName', 'D_ID__DealerEmail').annotate(
    #     document_total=Sum('TotalDocumentAmount'),
    #     vat_total=Sum('TotalVATAmountDocumentt'),
    #     doc_and_vat_total=Sum('TotalDocumentAmountWithVAT')
    # )
    # reference: https://stackoverflow.com/questions/13403609/how-to-group-by-and-aggregate-with-django

    unique_dealers = collect_unique_dealers_from_credit_notes(credit_notes)

    grouped_credit_notes = credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealers)

    totals_per_dealer = credit_notes_totals_per_dealer(grouped_credit_notes)

    return render(request, 'dashboard/dashboard.html', {
        'unique_dealers': unique_dealers,
        'grouped_credit_notes': grouped_credit_notes,
        'totals_per_dealer': totals_per_dealer
    })

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