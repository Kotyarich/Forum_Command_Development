from django.urls import path

from aggregator.views.dashboard import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('settings/', DashboardView.as_view(), name='settings'),
]
