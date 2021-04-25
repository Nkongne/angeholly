from django.urls import path,include
from django.contrib.auth import login, views as auth_views
from .views import become_vendor,vendor_admin,frontpage,add_product,edit_vendor,vendors,vendor
urlpatterns=[
    path("vendor/", become_vendor,name='become_vendor'),
    path("vendor_admin/", vendor_admin, name='vendor_admin'),
    path("edit_vendor/", edit_vendor, name='edit_vendor'),
    path("vendors/", vendors, name='vendors'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("login/",auth_views.LoginView.as_view(template_name='vendor/login.html'),name='login'),
    path("frontpage/", frontpage, name='frontpage'),
    path("<int:vendor_id>/", vendor, name='vendor'),
    path("add_product/", add_product, name='add_product'),
    ]
