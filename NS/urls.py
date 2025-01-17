
"""
URL configuration for NS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ALL VIEWS #
from pages.views import home_view, about_view
from products.views import shop_view, detail_view
from cart.views import cart_view
from authentication.views import register_view, login_view, logout_view, account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # user login and registration
    path('register/',register_view, name='register'),
    path('user_login/',login_view, name='login'),
    path('user_logout/',logout_view, name='logout'),
    
    # Account info
    path('account/',account_view, name='account'),
    
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('shop/<str:cat>/', shop_view, name='shop'),  
    path('single_product/<int:id>/', detail_view, name="single_product"),
    path('cart/', include('cart.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
