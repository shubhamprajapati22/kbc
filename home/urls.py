from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('game', views.game, name = 'game'),
    path('login', views.login, name = 'login'),
    path('contact', views.contact, name = 'contact'),
    path('profile', views.profile, name = 'profile'),
    path('signup', views.signup, name = 'signup')
]
