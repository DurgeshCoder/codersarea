"""blogs URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
urlpatterns = [
    path('upload_image/', upload_image),
    path('delete_image/', delete_image),
    path('admin/', admin.site.urls),
    path('', home),
    path("ads.txt", RedirectView.as_view(
        url=staticfiles_storage.url("ads.txt"))),
    path("<slug:technology_slug>/<slug:topic_slug>/", topic_manager),
    path('<slug:tech_slug>/', show_tech, name="show_tech")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
