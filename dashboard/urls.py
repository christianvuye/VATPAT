from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CustomLoginView,
    dashboard_view
)

# clean up all the code related to required login before being able to access the dashboard
# clean up all the different paths and urls too, because they are a mess.
urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('dashboard/', login_required(dashboard_view), name='dashboard')
]