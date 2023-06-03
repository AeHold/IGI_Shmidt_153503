from django.shortcuts import render, redirect
from django.views import View
from museumapp.forms import SignUpForm, LoginForm
import museumapp.models as models
import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import requests

class MainView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'museumapp/main.html', {})

class LoginView(View):
    form_class = LoginForm

    def post(self, req, *args, **kwargs):
        form = self.form_class(data = req.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(req, username =User.objects.get(email=email).username ,email = email, password = password)
            if user is not None:
                login(req, user)
                return redirect('/')
            else:
                return render(req, 'museumapp/login.html', {"form":form, "error":"User not found"})

        else:
            return render(req, 'museumapp/login.html', {"form":form, "error":form.errors.values()})

    def get(self, req, *args, **kwargs):
        if(req.user.is_authenticated):
            return redirect('/')
        form = self.form_class()
        return render(req, 'museumapp/login.html', {"form":form})

class SignUpView(View):
    form_class = SignUpForm

    def post(self, req, *args, **kwargs):
        form = self.form_class(data = req.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(email=email, password=password, username=first_name + " " + last_name)
            models.Profile.objects.create(phone_number=phone_number, user=user, post = models.Post.objects.get(name='intern'))
            login(req, user)
            
            return redirect('/')

        else:
            return render(req, 'museumapp/sign-up.html', {"form":form, "errors":form.errors.values()})

    def get(self, req, *args, **kwargs):
        if(req.user.is_authenticated):
            return redirect('/')

        form = self.form_class()
        return render(req, 'museumapp/sign-up.html', {"form":form})

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