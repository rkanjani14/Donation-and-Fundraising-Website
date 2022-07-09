from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from django.conf import settings
from decimal import Context, Decimal
# from paypal.standard.forms import PayPalPaymentsForm

from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import *


     
# Create your views here.

def home(request):
    return render(request, 'donation/home.html',)

def about(request):
    return render(request, 'donation/about.html',)

def contact(request):
    return render(request, 'donation/contact.html',)

def donation(request):
    return render(request,'donation/donation.html')

def persons_list(request):
    persons = Person.objects.all()
    context = {'persons':persons}
    return render(request, 'donation/personlist.html',context)

def process_payment(request):
    host = request.get_host()
    if request.method == 'POST':
        money = request.POST['amount']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        name = request.POST['name']

    person = {'name':name,'phone':phone,'email':email,'address':address,'money':money}
    global person1
    person1 = person
   
    
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': money,
        'item_name': 'test',
        'currency_code': 'INR',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'donation/process_payment.html', {'form': form})

@csrf_exempt
def payment_done(request):
    
    name = person1['name'] 
    phone = person1['phone'] 
    email = person1['email'] 
    address = person1['address'] 
    money = person1['money'] 

    p = Person(
        name=name,
        phone=phone,
        email=email,
        address=address,
        amount=money,
    )
    p.save()

    return render(request, 'donation/payment_done.html') 

@csrf_exempt
def payment_cancelled(request):
    return render(request, 'donation/payment_cancelled.html')