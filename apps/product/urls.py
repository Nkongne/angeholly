from django.urls import  path
from .views import product,cat,search

urlpatterns=[
            path("<slug:category_slug>/",cat, name='category'),
            path("<slug:category_slug>/<slug:product_slug>/",product, name='product'),

            path("search/", search, name='search')

        ]
