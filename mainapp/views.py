from django.shortcuts import render
from .models import *
def homepage(Request):
    products = Product.objects.all().order_by("-id")[0:12]
    maincategory=Maincategory.objects.all().order_by("-id")
    subcategory=Subcategory.objects.all().order_by("-id")
    brand=Brand.objects.all().order_by("-id")
    return render(Request,"index.html",{'products':products,'maincategory':maincategory,'subcategory':subcategory,'brand':brand})
def aboutpage(Request):
    return render(Request,"about.html")
def contactpage(Request):
    return render(Request,"contact.html")

def shoppage(Request,mc,sc,br):
    products=Product.objects.all()
    
    if(mc=="ALL" and sc=="ALL" and br=="ALL"):
        products=Product.objects.all().order_by("-id")
       
    elif(mc!="ALL" and sc=="ALL" and  br=="ALL"):
        products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
    elif(mc=="ALL" and sc!="ALL" and  br=="ALL"):
        products = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc=="ALL" or sc=="ALL" or  br!="ALL"):
        products = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-id")
    elif(mc!="ALL" or sc!="ALL" or  br=="ALL"):
        products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")
    elif(mc!="ALL" or sc=="ALL" or  br!="ALL"):
        products = Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")   
    elif(mc=="ALL" or sc!="ALL" or  br!="ALL"):
        products = Product.objects.filter(brand=Brand.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")
    else:
        products = Product.objects.filter(brand=Brand.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),maincategory=Maincategory.objects.get(name=mc)).order_by("-id").order_by("-id")   
    # products=Product.objects.all()
    maincategory=Maincategory.objects.all().order_by("-id")
    subcategory=Subcategory.objects.all().order_by("-id")
    brand=Brand.objects.all().order_by("-id")
    
    return render(Request,"shop.html",{'products':products,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br})
    
def singleproductpage(Request,id):
    product = Product.objects.get(id=id)
    return render(Request,"singleproduct.html",{'product':product})
def cartpage(Request):
    return render(Request,"cart.html")
def checkoutpage(Request):
    return render(Request,"checkout.html")
def confirmationpage(Request):
    return render(Request,"confirmation.html")
def loginpage(Request):
    return render(Request,"login.html")

def signuppage(Request):
    return render(Request,"signup.html")