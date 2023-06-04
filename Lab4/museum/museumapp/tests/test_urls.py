from django.test import SimpleTestCase
from django.urls import reverse, resolve
import museumapp.views as views

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func.__dict__,views.MainView.as_view().__dict__)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.__dict__,views.LoginView.as_view().__dict__)

    def test_signup_url_is_resolved(self):
        url = reverse('sign-up')
        self.assertEquals(resolve(url).func.__dict__,views.SignUpView.as_view().__dict__)

    def test_sessions_url_is_resolved(self):
        url = reverse('exhibitions')
        self.assertEquals(resolve(url).func.__dict__,views.ExhibitionsView.as_view().__dict__)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.__dict__,views.ProfileView.as_view().__dict__)

    def test_movies_url_is_resolved(self):
        url = reverse('schedule')
        self.assertEquals(resolve(url).func.__dict__,views.ScheduleView.as_view().__dict__)

    def test_some_movie_url_is_resolved(self):
        url = reverse('exhibition',args=[1])
        self.assertEquals(resolve(url).func.__dict__,views.ExhibitionView.as_view().__dict__)