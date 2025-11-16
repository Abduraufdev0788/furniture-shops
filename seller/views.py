from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
import json
from products.models import Product
from .models import Seller
from users.models import User
from products.models import Product
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def seller_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        tel = request.POST.get("tel")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        shop_name = request.POST.get("shop_name")


        if password != confirm_password:
            return HttpResponse("Parollar mos kelmadi!", status=400)


        if User.objects.filter(tel=tel).exists():
            return HttpResponse("Bu raqam buyerga tegishli!", status=403)

       
        if Seller.objects.filter(tel=tel).exists():
            return HttpResponse("Bu telefon raqam boshqa sellerga tegishli!", status=403)

     
        hashed_password = hash_password(password)

    
        seller = Seller(
            first_name=first_name,
            last_name=last_name,
            tel=tel,
            password=hashed_password,
            confirm_password=hashed_password,
            shop_name=shop_name
        )
        seller.save()


        request.session['seller_id'] = seller.id

        return redirect("seller:dashboard") 

    return render(request, "seller_register.html")



def login_seller(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        tel = request.POST.get("tel")
        password = request.POST.get("password")

       
        hashed_password = hash_password(password)

       
        if User.objects.filter(tel=tel).exists():
            return HttpResponse("Bu telefon raqam buyerga tegishli!", status=403)

        
        if not Seller.objects.filter(tel=tel).exists():
            return HttpResponse("Seller topilmadi!", status=404)

        
        try:
            seller = Seller.objects.get(tel=tel, password=hashed_password)
            request.session['seller_id'] = seller.id
            return redirect("seller:dashboard") 
        except Seller.DoesNotExist:
            return HttpResponse("Telefon yoki parol noto'g'ri!", status=401)

    return render(request, "seller_login.html")

def seller_dashboard(request: HttpRequest) -> HttpResponse:
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect("seller:login") 

    try:
        seller = Seller.objects.get(id=seller_id)
        profile ={
            "seller": seller
        }
        
    except Seller.DoesNotExist:
        return redirect("seller:login") 

    return render(request, "seller_dashboard.html", profile)

def add_product(request: HttpRequest) -> HttpResponse:
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect("seller:login") 

    try:
        seller = Seller.objects.get(id=seller_id)
    except Seller.DoesNotExist:
        return redirect("seller:login") 

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")
        image = request.FILES.get("image")

        product = Product(
            seller_product=seller,
            name=name,
            description=description,
            price=price,
            category=category,
            image=image
        )
        product.save()

        return redirect("seller:view_products") 

    return render(request, "seller_add_product.html")

def view_products(request: HttpRequest) -> HttpResponse:
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect("seller:login") 

    try:
        seller = Seller.objects.get(id=seller_id)
    except Seller.DoesNotExist:
        return redirect("seller:login") 

    products = Product.objects.filter(seller_product=seller)

    context = {
        "products": products
    }

    return render(request = request, template_name="seller_view_products.html", context=context)

def edit_product(request: HttpRequest, product_id: int) -> HttpResponse:
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect("seller:login") 

    try:
        seller = Seller.objects.get(id=seller_id)
    except Seller.DoesNotExist:
        return redirect("seller:login") 

    try:
        product = Product.objects.get(id=product_id, seller_product=seller)
    except Product.DoesNotExist:
        return HttpResponse("Mahsulot topilmadi yoki sizga tegishli emas.", status=404)

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.category = request.POST.get("category")
        if "image" in request.FILES:
            product.image = request.FILES.get("image")
        product.save()
        return redirect("seller:view_products")

    context = {
        "product": product
    }
    return render(request, "seller_edit_product.html", context)

def delete_product(request:HttpRequest, product_id: int)->HttpResponse:
    seller_id = request.session.get("seller_id")
    if not seller_id:
        return redirect("seller:login")

    try:
        seller = Seller.objects.get(id=seller_id)
    except Seller.DoesNotExist:
        return redirect("seller:login")

    try:
        product = Product.objects.get(id=product_id, seller_product=seller)
    except Product.DoesNotExist:
        return HttpResponse("Mahsulot topilmadi yoki sizga tegishli emas.", status=404)

    product.delete()
    return redirect("seller:view_products")

def seller_profile(request:HttpRequest)->HttpResponse:
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect("seller:login")
    try:
        seller = Seller.objects.get(id = seller_id)
        context = {
            "seller":seller
        }
    except Seller.DoesNotExist:
        return redirect("seller:login")
    
    return render(request=request, template_name="seller_profile.html", context=context)

def edit_profile(request: HttpRequest) -> HttpResponse:
    seller_id = request.session.get("seller_id")
    if not seller_id:
        return redirect("seller:login")

    seller = Seller.objects.get(id=seller_id)

    if request.method == "POST":
        seller.first_name = request.POST.get("first_name")
        seller.last_name = request.POST.get("last_name")
        seller.tel = request.POST.get("tel")
        seller.shop_name = request.POST.get("shop_name")
        seller.save()
        return redirect("seller:seller_profile")

    return render(request, "seller_edit_profile.html", {"seller": seller})
    
def logout(request:HttpRequest)->HttpResponse:
    return redirect("seller:login")

    
   

        