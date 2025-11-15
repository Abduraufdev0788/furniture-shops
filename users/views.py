from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
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
