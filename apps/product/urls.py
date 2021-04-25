from django.urls import  path
from .views import product,cat,search

urlpatterns=[
             path("C<slug:category_slug>/", cat, name='category'),
            path("P<slug:category_slug>/<slug:product_slug>/",product, name='product'),

            path("search/", search, name='search')

        ]
