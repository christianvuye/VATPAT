from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CustomLoginView,
    dashboard_view
)

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('dashboard/', login_required(dashboard_view), name='dashboard')
]