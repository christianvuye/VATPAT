from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CustomLoginView,
    dashboard_view,
    dashboard_view_acknowledgements
)

"""
Sort out the URL patterns for the dashboard app, decide which pages to see first and how navigation will work.
"""
urlpatterns = [
    # You have a login view linked here and in VATPAT urls, with the same name. Do you really need both?
    # If not, you should remove the one that is not used. If you do, make sure each has a distinct name.
    path('', CustomLoginView.as_view(), name='login'),
    # I normally put the login_required on the view itself, which seems slightly better to me, since it is
    # possible to hook up a view to more than one path and you would not want to risk exposing it.
    path('dashboard/', login_required(dashboard_view), name='dashboard'),
    path('dashboard_view_acknowledgements/', login_required(dashboard_view_acknowledgements), name='dashboard_view_acknowledgements')
]