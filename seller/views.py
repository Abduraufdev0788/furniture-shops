from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Seller

def seller_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        tel = request.POST.get("tel")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        shop_name = request.POST.get("shop_name")

        if password != confirm_password:
            return HttpResponse("Passwords do not match", status=400)

        seller = Seller(
            first_name=first_name,
            last_name=last_name,
            tel=tel,
            password=password,
            confirm_password=confirm_password,
            shop_name=shop_name
        )
        seller.save()
        return HttpResponse("Seller registered successfully", status=201)
    
    return render(request, "seller/register.html")