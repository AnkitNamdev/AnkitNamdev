from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .models import BillingAd

# Create your views here.
def home(req):
    return render(req,'product/base.html')

def home1(req):
    return render(req,'product/index.html')

def sports(req):
    return render(req,'product/sports.html')

def dailyproduct(req):
    return render(req,'product/daily.html')

def allitem(req):
    data=Product.objects.all()
    return render(req,'product/allitems.html',{'data':data})

def buy(req,id,price,av):
    if req.method=="POST":
        data=Product.objects.get(pk=id)
        q=int(req.POST.get('quan'))
        av=int(av)-q
        price=float(price)
        total=q*price
        p1=Product.objects.filter(pk=id).update(available=av)
        return render(req,'product/final.html',{'i':data,'q':q,'total':total,'available':av})


def bill(req):
    # if req.method=="POST":

        
    return render(req,'product/billing.html')


def delivery(req):
    if req.method=="POST":
        cusn=req.POST.get('cn')
        cusa=req.POST.get('ca')
        cusp=req.POST.get('cp')
        cusm=req.POST.get('cm')
        bil=BillingAd(name=cusn,Address=cusa,pin_Code=cusp,Mobile_No=cusm)
        bil.save()
        return render(req,'product/billing.html')
    


def search(req):
    if req.method=="POST":
        searchitem=req.POST.get('searchdata')
        data=Product.objects.filter(name=searchitem)
        if data:
            return render(req,'product/final.html',{'i':data})
        else:
             return render(req,'product/final.html',{'msg':'no data available'})

