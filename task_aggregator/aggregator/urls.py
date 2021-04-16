from django.urls import path

from aggregator.views.dashboard import DashboardView
from aggregator.views.settings import SettingsView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('settings/', SettingsView.as_view(), name='settings'),
]
