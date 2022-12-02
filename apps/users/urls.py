import django.urls

from . import views

urlpatterns = [
    django.urls.path('register', views.register, name='register'),
    django.urls.path('login', views.login, name='login'),
    django.urls.path('dashboard', views.dashboard, name='dashboard'),
    django.urls.path('logout', views.logout, name='logout')
]