from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages import success,error
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
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
    if(Request.method=="POST"):
        username=Request.POST.get("username")
        password=Request.POST.get("password")
        user=authenticate(username=username,password=password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
            
        else:
            error(Request,"invalid user name and password!!!!")
    return render(Request,"login.html")

    

def signuppage(Request):
    if(Request.method=="POST"):
        password=Request.POST.get("password")
        cpassword=Request.POST.get("cpassword")
        if(password==cpassword):
            username=Request.POST.get("username")
            email=Request.POST.get("email")
            name=Request.POST.get("name")
            try:
                User.objects.create_user(username=username,email=email,password=password,first_name=name)
                    
                phone=Request.POST.get("phone")
                b=Buyer()
                b.name=name
                b.email=email
                b.username=username
                b.phone=phone
                b.save()
                return HttpResponseRedirect("/login")
            except:
             error(Request,"username already taken")
        else:
            error(Request," Password and Confirm password does't matched...")
    return render(Request,"signup.html")


def profilepage(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    username=Request.user.username
    try:
        buyer=Buyer.objects.get(username=username)
        return render(Request,"profile.html",{'buyer':buyer})
    except:
        return HttpResponseRedirect("/login/")
def updateprofile(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    username=Request.user.username
    try:
        buyer=Buyer.objects.get(username=username)
        if(Request.method=="POST"):
            buyer.name=Request.POST.get("name")
            buyer.email=Request.POST.get("email")
            buyer.phone=Request.POST.get("phone")
            buyer.pin=Request.POST.get("pin")
            buyer.address=Request.POST.get("address")
            buyer.state=Request.POST.get("state")
            buyer.city=Request.POST.get("city")
            if(Request.FILES.get("pic")):
                buyer.pic=Request.FILES.get("pic")
            buyer.save()
            return HttpResponseRedirect("/profile")
        
        return render(Request,"updateprofile.html",{'buyer':buyer})
    except:
        return HttpResponseRedirect("/login/")
def logoutpage(Request):
    logout(Request)
    return HttpResponseRedirect("/login/")