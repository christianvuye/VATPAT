"""
URL configuration for VATPAT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView

# clean up all the code related to required login before being able to access the dashboard
# clean up all the different paths and urls too, because they are a mess.
urlpatterns = [
    path('admin/', admin.site.urls),
    # You have a login view linked here and in dashboard urls, with the same name. Do you really need both?
    # If not, you should remove the one that is not used. If you do, make sure each has a distinct name.
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Interesting -- I actually didn't know about next_page. I have always used the redirect url settings
    # https://docs.djangoproject.com/en/5.0/ref/settings/#login-redirect-url
    # https://docs.djangoproject.com/en/5.0/ref/settings/#logout-redirect-url
    path('logout/', auth_views.LogoutView.as_view(next_page='/dashboard/'), name='logout'),
    path('dashboard/', include('dashboard.urls')),
    # As long as dashboard requires login, which it does, it's normal to redirect to that
    path('', RedirectView.as_view(url='dashboard/', permanent=True)), # Homepage should be login probably, but for now redirect to dashboard
]