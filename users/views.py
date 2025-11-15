from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import User
import requests
from dotenv import load_dotenv
import os

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")
TOKEN = os.getenv("TOKEN")


def bosh_sahifa(request: HttpRequest) -> HttpResponse:
    return render(request = request, template_name = "bosh_sahifa.html")

def aloqa(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        message_text = f"Ism: {name}\nTelefon: {phone}\nCategoriyasi: {subject}\nXabar: {message}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
        "chat_id": CHAT_ID,
        "text": message_text
     }
        requests.post(url, data=payload)

        return redirect("bosh_sahifa")
       
    return render(request = request, template_name = "aloqa.html")


def registratsiya(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_user_data = User(
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            tel = request.POST.get("tel"),
            password = request.POST.get("password"),
            confirm_password = request.POST.get("confirm_password"),
        )
        if new_user_data.password != new_user_data.confirm_password :
            return HttpResponse("Parollar mos emas!")
        if User.objects.filter(tel=new_user_data.tel).exists():
            return HttpResponse("Bu telefon raqam allaqachon ro'yxatdan o'tgan!")
              

        new_user_data.save()
        return HttpResponse("Ro'yxatdan o'tish muvaffaqiyatli amalga oshirildi!")

    return render(request = request, template_name = "registratsiya.html")


def login(request: HttpRequest) -> HttpResponse:
    return render(request = request, template_name = "login.html")