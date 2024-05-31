from django.urls import path
from .views import (
    CustomLoginView,
    dashboard_view
)

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('dashboard', dashboard_view, name='dashboard')
]