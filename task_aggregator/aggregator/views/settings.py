from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from aggregator.models import Token, Map


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'settings.html'
    login_url = 'login'
    redirect_field_name = 'settings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        tokens = Token.objects.filter(user=user)
        context['tokens'] = tokens
        context['map'] = tokens[0].map

        return context
