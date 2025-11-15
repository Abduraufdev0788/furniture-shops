from django.urls import path
from .views import bosh_sahifa, aloqa

urlpatterns = [
    path('', bosh_sahifa, name='bosh_sahifa'),
    path("aloqa/", aloqa, name="aloqa"),
]