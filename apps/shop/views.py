from django.shortcuts import render
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
#from twilio.rest import Client
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse, FileResponse, Http404
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from apps.product.models import Product
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    return HttpResponse(render(request, 'index.html'))
def customercart(request):
    infos= _("informations about my cart")
    return HttpResponse(render(request, 'shop/carte.html', {'infos':infos}))
def singleproduct(request):
    return HttpResponse(render(request,'shop/single-product.html'))
def shoping(request):
    return HttpResponse(render(request,'shop/shop.html'))
def checkout(request):
    return HttpResponse(render(request,'shop/checkout.html'))
def lang_select(request):
    return HttpResponse(render(request,'shop/lang_select.html'))
def pdfr (request):

    file = open('static/pdf/Nkongne_Resume.pdf', "rb")
    pdf = file.read()

    return HttpResponse(pdf, 'application/pdf')
def frontpage(request):
    newest_product=Product.objects.all()[0:8]
    return HttpResponse(render(request, 'frontpage.html',{'newest_product':newest_product}))
def contact(request):
    return HttpResponse(render(request, 'shop/contact.html'))