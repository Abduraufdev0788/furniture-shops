from django.urls import path
from .views import bosh_sahifa, aloqa, registratsiya, login, profile, product_detail, savatcha, savatcha_bolimi

urlpatterns = [
    path('', bosh_sahifa, name='bosh_sahifa'),
    path("registratsiya/", registratsiya, name="registratsiya"),
    path("login/", login, name="login"),
    path("aloqa/", aloqa, name="aloqa"),
    path("profile/", profile, name="profile"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path("savatcha/<int:product_id>/", savatcha, name="savatcha"),
    path("savatcha/", savatcha_bolimi, name="savatcha_bolimi"),
]