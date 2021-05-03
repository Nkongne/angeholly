from django.conf.urls.i18n import i18n_patterns
from django.urls import path,include

from .views import index,customercart,singleproduct,shoping,checkout,lang_select,contact,frontpage,pdfr
app_name="shop"

urlpatterns=[
    path("", index,name='home'),

    path("cart/", customercart,name='cart'),
    path("singleproduct/", singleproduct,name='singleproduct'),
    path("shoping/", shoping, name='shoping'),
    path("checkout/", checkout,name='checkout'),
    path("language/",lang_select, name='lang_select'),
    path("contact/", contact,name='contact'),
    path("", frontpage, name='frontpage'),
    path('', pdfr, name='pdfr')
    ]

