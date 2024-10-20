from django.contrib import admin
from django.urls import path
from mainapp import views as mainApp
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homepage,name="homepage"),
    path('about/',mainApp.aboutpage,name="about"),
    path('cart/',mainApp.cartpage,name="cart"),
    path('checkout/',mainApp.checkoutpage,name="checkout"),
    path('confirmation/',mainApp.confirmationpage,name="confirmation"),
    path('contact/',mainApp.contactpage,name="contact"),
    path('profile/',mainApp.profilepage,name="profile"),
    path('updateprofile/',mainApp.updateprofile,name="updateprofile"),
    path('logout/',mainApp.logoutpage,name="logout"),
    path('login/',mainApp.loginpage,name="login"),
    path('signup/',mainApp.signuppage,name="signup"),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shoppage,name="shop"),
    path('singleproduct/<int:id>/',mainApp.singleproductpage,name="singleproduct"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 