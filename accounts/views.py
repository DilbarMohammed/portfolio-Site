from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import SignupForm, StyledAuthenticationForm


class UserLoginView(LoginView):
    authentication_form = StyledAuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "page_title": "Login | Portfolio",
            "meta_description": "Login to your portfolio account.",
        }


class SignupView(FormView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("core:home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:home")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Account created successfully. Welcome in.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "page_title": "Sign Up | Portfolio",
            "meta_description": "Create a portfolio account.",
        }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("core:home")
