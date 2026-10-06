"""
Authentication views for ArSa.
"""
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from .forms import LoginForm


class ArSaLoginView(LoginView):
    """Custom login view with romantic styling."""
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dates:dashboard')

    def form_valid(self, form):
        messages.success(
            self.request,
            f"Welcome back, {form.get_user().get_display_name()} ❤️"
        )
        return super().form_valid(form)


class LogoutView(View):
    """Simple logout."""
    def post(self, request):
        logout(request)
        messages.info(request, "You have been logged out. See you soon ❤️")
        return redirect('accounts:login')

    def get(self, request):
        # Allow GET for convenience
        logout(request)
        messages.info(request, "You have been logged out. See you soon ❤️")
        return redirect('accounts:login')
