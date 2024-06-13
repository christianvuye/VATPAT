from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from .views import (
    CustomLoginView,
    dashboard_view,
    dashboard_view_acknowledgements,
    index,
    call_downstream_api
)

"""
Sort out the URL patterns for the dashboard app, decide which pages to see first and how navigation will work.
"""
urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard_view, name='Credit Note Overview'),
    path('dashboard_view_acknowledgements/', dashboard_view_acknowledgements, name='Acknowledgement Tracker'),
    path("azure-signin/", include("azure_signin.urls", namespace="azure_signin")),
    settings.AUTH.urlpattern,
    path('index', index),
    path("call_downstream_api", call_downstream_api),
    path('admin/', admin.site.urls),
]