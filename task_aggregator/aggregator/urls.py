from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import RedirectView

from aggregator.views.dashboard import DashboardView
from aggregator.views.settings import SettingsView

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard', permanent=True), name='index'),

    path('dashboard/', login_required(DashboardView.as_view()), name='dashboard'),
    path('settings/', login_required(SettingsView.as_view()), name='settings'),
]
