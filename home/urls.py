from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('game/', views.game, name = 'game'),
    path('contact/', views.contact, name = 'contact'),
    path('profile/', views.profile, name = 'profile'),
]
