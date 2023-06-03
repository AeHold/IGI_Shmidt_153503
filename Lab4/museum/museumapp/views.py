from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm, LoginForm
import museumapp.models
import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import requests

class MainView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/main.html', {})

class LoginView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/login.html', {})

class SignUpView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/sign-up.html', {})

class ExhibitionsView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/exhibitions.html', {})

class ExcursionsView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/excursions.html', {})

class ExponatesView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/exponates.html', {})

class ProfileView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/profile.html', {})

class ScheduleView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/schedule.html', {})

class ExponateView(View):
    def get(self, req, *args, exponate_id, **kwargs):
        return render(req, 'museumapp/exponate.html', {})

class ExhibitionView(View):
    def get(self, req, *args, exhibition_id, **kwargs):
        return render(req, 'museumapp/exhibition.html', {})