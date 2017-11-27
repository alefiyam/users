"""users_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 	url(r'^signup/$', views.signup, name='signup'),
 	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
 	url(r'^home/$', views.home, name='home'),
 	url(r'^list_users/$', views.list_users, name='list_users'),
 	url(r'^sort/$', views.sort, name='sort'),
 	# url(r'^auth/', include('auth.urls')),
    url(r'^admin/', admin.site.urls),
]