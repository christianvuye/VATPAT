from django.shortcuts import render
from .models import Dealers
from .utils import get_previous_months
from django.contrib.auth.views import LoginView
#from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    """
    Custom login view that uses the login.html template.
    """
    template_name = 'login.html'

# Django recommends using function-based views over class-based views when the view is simple.
# In this case, the view is simple and does not require any additional methods or attributes.
# Therefore, we use a function-based view. 
# But check with Jessamyn what she thinks is the right approach.

# clean up all the code related to required login before being able to access the dashboard
#@login_required
def dashboard_view(request):
    """
    Renders the dashboard view with the data from the previous month.
    """

    return render(request, 'dashboard/dashboard.html', 
                  )

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