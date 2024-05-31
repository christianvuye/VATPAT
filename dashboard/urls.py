from django.urls import path
from .views import (
    CustomLoginView,
    dashboard_view
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', dashboard_view, name='dashboard')
]