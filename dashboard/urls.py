from django.urls import path
from .views import (
    dashboard_view, 
    credit_notes_previous_month_view,
    credit_notes_previous_month_grouped_by_dealer_view
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('credit_notes_previous_month/', 
         credit_notes_previous_month_view, 
         name='credit_notes_previous_month'),
    path('credit_notes_previous_month_grouped_by_dealer/', 
         credit_notes_previous_month_grouped_by_dealer_view, 
         name='credit_notes_previous_month_grouped_by_dealer')
]