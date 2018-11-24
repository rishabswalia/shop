"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [    
    url(r'^admin/', admin.site.urls),
    url('', include('home.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^adminpanel/', include('adminpanel.urls')),
    url(r'^thankyou/',include('thankyou.urls')),
    url(r'^login/',include('login.urls')),
    url(r'^signup/',include('signup.urls')),
    url(r'^shopall/',include('product_cat.urls')),
    url(r'^contact/',include('contactus.urls')),
]