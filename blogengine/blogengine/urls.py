"""blogengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
#from .views import hello
from .views import redirect_blog
from blog.views import register, profile, logoutUser, cart_view

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
	path('register/', register, name='register'),
	path('', include("django.contrib.auth.urls")),
	path('profile/', profile, name='profile'),
	path('logout/', logoutUser, name='logout'),
	path('cart/', cart_view, name='cart'),
	
	

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)