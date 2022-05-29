"""getreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path
from getreg import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#development only
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output,name="script"),
    url(r'^delete', views.delete,name="delete"),
    url(r'^upload2', views.delete,name="upload2"),
]

urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

