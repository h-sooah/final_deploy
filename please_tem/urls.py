"""please_tem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import blog.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')),
    path('notice/', blog.views.notice, name="notice"),
    path('blog/<int:blog_id>/',blog.views.detail, name="detail"),
    path('blog/buy/<int:buy_id>',blog.views.buy_detail, name="buy_detail"),
    path('buy/', blog.views.buy, name = "buy"),
    path('sell/', blog.views.sell, name = "sell"),
    path('blog/sell/<int:sell_id>', blog.views.sell_detail, name = "sell_detail"),
    path('blog/buy/buy_form', blog.views.buy_form, name = "buy_form"),
    path('buying',blog.views.buying, name = "buying"),
    path('blog/sell/sell_form', blog.views.sell_form, name = "sell_form"),
    path('selling',blog.views.selling, name = "selling"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
