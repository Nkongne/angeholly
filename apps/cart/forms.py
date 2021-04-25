from django import  forms
class CheckoutForm(forms.Form):
    nom=forms.CharField(max_length=255)
    prenom = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone=forms.CharField(max_length=255)
    address=forms.CharField(max_length=255)
    zipcode = forms.CharField(max_length=255)
    place = forms.CharField(max_length=255)
    stripe_token = forms.CharField(max_length=255)