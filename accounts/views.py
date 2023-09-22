from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .form import SignUpForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = 'login'
    template_name = 'registration/signup.html'
