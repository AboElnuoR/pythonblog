"""pythonblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
	url(r'^$',index),
	url(r'^latest_5$',latest_5),
	url(r'^single/(?P<post_id>[0-9]+)/$',single),
    url(r'^registe$',register),
    url(r'^login$',login),
<<<<<<< HEAD
=======
    url(r'^signin$',signin),
    url(r'^loggedin$',loggedin),
    url(r'^invalid$',invalid),
    url(r'^logout_view$',logout_view),
>>>>>>> 8817bb3f2d6b76d8f758bca09504e256f0cfac79
]
