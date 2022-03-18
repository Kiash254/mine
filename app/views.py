from django.shortcuts import render
from matplotlib.style import context
from .models import Workerdetail,Companies,Product,Products,HeadQ,Area,Shop,SuperheadQ
# Create your views here.

def worker(request):
    worker=Workerdetail.objects.all()

    context={
        "worker":worker
    }
    return render(request,"worker.html")
def company(request):
    company=Companies.objects.all()

    context={
        "company":company
    }
    return render(request,"company.html")

def product(request):
    product=Product.objects.all()

    context={
        "product":product
    }
    return render(request,"product.html",context)

def products(request):
    products=Products.objects.all()

    context={
        "products":products
    }
    return render(request,"products.html",context)

def head(request):
    head=HeadQ.objects.all()

    context={
        "head":head
    }
    return render(request,"head.html",context)


def area(request):
    area=Area.objects.all()

    context={
        "area":area
    }
    return render(request,"area.html",context)


def shop(request):
    shop=Shop.objects.all()

    context={
        "shiop":shop
    }
    return render(request,"shop.html",context)

def super(request):
    super=SuperheadQ.objects.all()

    context={
        "super":super
    }
    return render(request,"super.html")