from django.urls import path
from .views import seller_register, login_seller, seller_dashboard, add_product, view_products, edit_product, delete_product, seller_profile, edit_profile, logout

app_name = "seller"

urlpatterns = [
    path('register/', seller_register, name='registratsiya'),
    path('login/', login_seller, name='login'),
    path('dashboard/', seller_dashboard, name='dashboard'),
    path('add_product/', add_product, name='add_product'),
    path("view_products/", view_products, name="view_products"),
    path("edit_product/<int:product_id>/", edit_product, name="edit_product"),
    path("delete_product/<int:product_id>/", delete_product, name="delete_product"),
    path("seller_profile/", seller_profile, name="seller_profile"),
    path("seller_edit/", edit_profile, name="seller_edit"),
    path("logout/",logout, name="logout")
]