from django.urls import  path
from .views import category, search, product

urlpatterns=[
            path("search/", search, name='search'),
            path("P<slug:category_slug>/<slug:product_slug>/", product, name='product'),
            path("C<slug:category_slug>/",category, name='category')


        ]
