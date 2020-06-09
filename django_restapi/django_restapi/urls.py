"""django_restapi URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/children/', include('api_children.urls'), name='api_children'),
    path('api/result/', include('api_result.urls'), name='api_result'),
    path('api/comments/', include('api_comments.urls'), name='api_comments'),
    path('api/treemodel/', include('api_comments.urls'), name='api_comments'),
    path('api/appuser/', include('api_user.urls'), name='api_user'),
    url(r'^image/', include('image_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

