from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)
