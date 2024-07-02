from django.urls import path
from .views import (
    CustomLoginView,
    dashboard_view,
    dashboard_view_acknowledgements,
    dashboard_view_month_year
)

"""
Sort out the URL patterns for the dashboard app, decide which pages to see first and how navigation will work.
"""
urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard_view, name='Credit Note Overview'),
    path('dashboard_view_acknowledgements/', dashboard_view_acknowledgements, name='Acknowledgement Tracker'),
    path('dashboard_view_month_year/', dashboard_view_month_year, name='Month Year Selector'),
]