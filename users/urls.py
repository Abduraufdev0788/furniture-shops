from django.urls import path
from .views import bosh_sahifa, aloqa, registratsiya, login

urlpatterns = [
    path('', bosh_sahifa, name='bosh_sahifa'),
    path("registratsiya/", registratsiya, name="registratsiya"),
    path("login/", login, name="login"),
    path("aloqa/", aloqa, name="aloqa"),
]