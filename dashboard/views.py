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

"""
Create a common base.html that all templates inherit from.

This guarantees a consistent look and feel on your site, ensures you are using the same versions of

JS libraries, and generally makes your life MUCH easier. I also recommend having your custom JS in .js

files that are loaded into the template via static. This gives you options like linting the JS, 

compressing it, loading it from a CDN, etc.

Note that the base template typically needs blocks to allow inheritors to enter their own title,

head content, body content, and js/footer content.
"""

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