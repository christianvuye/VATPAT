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
    path('', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard_view_acknowledgements/', dashboard_view_acknowledgements, name='dashboard_view_acknowledgements')
]