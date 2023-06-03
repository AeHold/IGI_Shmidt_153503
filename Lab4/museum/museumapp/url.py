from django.urls import path, re_path
from museumapp import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('login/', views.LoginView.as_view(), name = "login"),
    path('sign-up/', views.SignUpView.as_view(), name = "sign-up"),
    path('profile/', views.ProfileView.as_view(), name = "profile"),
    path('schedule/', views.ScheduleView.as_view(), name = "schedule"),
    path('exponates/', views.ExponatesView.as_view(), name = "exponates"),
    path('exhibitions/', views.ExhibitionsView.as_view(), name = "exhibitions"),
    re_path(r'^exponate/(?P<exponate_id>\d+)/$', views.ExponateView.as_view(), name = "exponate"),
    re_path(r'^exhibition/(?P<exhibition_id>\d+)/$', views.ExhibitionView.as_view(), name = "exhibition"),
]