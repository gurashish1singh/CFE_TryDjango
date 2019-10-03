"""trydjango URL Configuration

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

# Media URls
from django.conf import settings
from django.conf.urls.static import static

# Posts app
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Posts URLs
    path('posts/',posts_list, name='list'),
    path('posts/create/',posts_create),
    path('posts/<slug>/',posts_detail, name = 'detail'),
    path('posts/<slug>/update',posts_update, name = 'update'),
    path('posts/<slug>/delete/',posts_delete),

]

# Media URLs
urlpatterns = urlpatterns + static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
