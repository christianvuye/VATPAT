from django.urls import path
from .views import (
    dashboard_view, 
    credit_notes_previous_month_view,
    dashboard_2_view
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard_2/', dashboard_2_view, name='dashboard_2')
]