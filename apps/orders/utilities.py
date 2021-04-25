from apps.cart.cart import Cart
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Order,OrderItem

def checkout(request,nom,prenom,email,zipcode,address,place,phone,amount):
    order=Order.objects.create(nom=nom,prenom=prenom,email=email,zipcode=zipcode,address=address,place=place,phone=phone,paid_amount=amount)
    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'],vendor=item['product'].vendor,price=item['product'].price,quantity=item['quantity'])
        order.vendors.add(item['product'].vendor)
    return order
def notify_vendor(order):
    from_email=settings.EMAIL_HOST_USER

    for vendor in order.vendors.all():
        to_email=vendor.cree_par
        subject='New order'
        text_content='you have a new order!'
        html_content=render_to_string('order/email_notify_vendor.html',{'order':order,'vendor':vendor})

        msg = EmailMultiAlternatives(subject,text_content,from_email,[to_email])
        msg.attach_alternative(html_content,'text/html')
        msg.send()


def notify_customer(order):
    from_email = settings.EMAIL_HOST_USER
    to_email = order.email
    subject = 'order notification'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


