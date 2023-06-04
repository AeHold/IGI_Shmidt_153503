from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUpTestData():
        call_command('loaddata', 'museum_testdata.json')

    def setUp(self):
        self.client = Client()

    def test_main_GET_is_authorized(self):
        User.objects.create_user(username='valid', password='valid')
        self.client.login(username='valid', password='valid')   
        response = self.client.get(reverse("main"))     

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/main.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_main_GET_is_unauthorized(self):  
        response = self.client.get(reverse("main"))     

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/main.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_login_GET_is_authorized(self):
        User.objects.create_user(username='valid', password='valid')
        self.client.login(username='valid', password='valid')   
        response = self.client.get(reverse("login"))     

        self.assertEqual(response.status_code, 302)

    def test_login_GET_is_unauthorized(self): 
        response = self.client.get(reverse("login"))     

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/login.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_login_POST_valid_user(self):
        User.objects.create_user(username='valid',email='valid@mail.ru',password='valid')

        response = self.client.post(reverse('login'),{
            'email': 'valid@mail.ru',
            'password': 'valid'
        })

        self.assertEqual(response.status_code, 302)
    
    def test_login_POST_invalid_user(self):
        User.objects.create_user(username='valid',password='valid')

        response = self.client.post(reverse('login'),{
            'username': 'invalid',
            'password': 'invalid'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/login.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_login_POST_invalid_form(self):
        User.objects.create_user(username='valid',password='valid')

        response = self.client.post(reverse('login'),{
            'username': 'invalid'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/login.html')
        self.assertTemplateUsed(response,'museumapp/base.html') 

    def test_signUp_GET_is_authorized(self):
        User.objects.create_user(username='valid', password='valid')
        self.client.login(username='valid', password='valid')   
        response = self.client.get(reverse("sign-up"))     

        self.assertEqual(response.status_code, 302)

    def test_signUp_GET_is_unauthorized(self): 
        response = self.client.get(reverse("sign-up"))     

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/sign-up.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_signUp_POST_valid_form(self):

        response = self.client.post(reverse('sign-up'),{
            'email': 'valid@mail.ru',
            'password': 'valid123',
            'password_confirmation': 'valid123',
            'phone_number':'+375259514261',
            'first_name':'Aboba',
            'last_name':'Amoga'
        })

        self.assertEqual(response.status_code, 302)

    def test_signUp_POST_invalid_form(self):
        User.objects.create_user(username='valid',password='valid')

        response = self.client.post(reverse('sign-up'),{
            'username': 'invalid'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/sign-up.html')
        self.assertTemplateUsed(response,'museumapp/base.html')       

    def test_exhibitions_GET(self):
        response = self.client.get(reverse('exhibitions'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/exhibitions.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_schedule_GET_unfilter(self):
        response = self.client.get(reverse('schedule'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/schedule.html')
        self.assertTemplateUsed(response,'museumapp/base.html')

    def test_schedule_GET_filter(self):
        response = self.client.get(reverse('schedule'), {
            'dfrom': '2023-05-05',
            'dto':'2023-05-12',
            'admin': 'on',
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/schedule.html')
        self.assertTemplateUsed(response,'museumapp/base.html')
    
    def test_exhibition_GET(self):
        response = self.client.get(reverse('exhibition',args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'museumapp/exhibition.html')
        self.assertTemplateUsed(response,'museumapp/base.html')