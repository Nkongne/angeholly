import stripe
from django.shortcuts import render,redirect
# Create your views here.
from .cart import Cart
from django.conf import settings
from django.contrib import messages
from .forms import CheckoutForm
from apps.orders.utilities import checkout,notify_vendor,notify_customer

def cart_detail(request):
    cart=Cart(request)

    if request.method=='POST':
        form=CheckoutForm(request.POST)
        if form.is_valid():
            stripe.api_key=settings.STRIPE_SECRET_KEY
            stripe_token=form.cleaned_data['stripe_token']
            try:
                charge=stripe.Charge.create(
                    amount=int(cart.get_total_cost()*100),
                    currency='USD',
                    description='charge from AngeHolly Ecommerce',
                    source=stripe_token
                )
                nom = form.cleaned_data['nom']
                prenom = form.cleaned_data['prenom']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order=checkout(nom,prenom,email,phone,address,zipcode,place,cart.get_total_cost)
                cart.clear()
                notify_customer(order)
                notify_vendor(order)
                return redirect('success')
            except Exception:
                messages.error(request,'there was something wrong!')

    else:
        form=CheckoutForm()




    remove_from_cart=request.GET.get('remove_from_cart','')
    change_quantity=request.GET.get('change_quantity','')
    quantity = request.GET.get('quantity', '0')
    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')
    if change_quantity:
        cart.add(change_quantity,quantity,True)
        return redirect('cart')
    return render(request,'cart/cart.html',{'form':form, 'stripe_pub_key':settings.STRIPE_PUB_KEY})
def success(request):
    return render(request, 'cart/success.html')