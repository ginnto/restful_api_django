"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from myapp import views
from myapp.views import TaskViewset,CreateuserView              #IMPORT VIEWSET FROM MYAPP VIEWS
from django.conf.urls.static import static
# router=routers.DefaultRouter()     #this the default rest router no change
router=routers.SimpleRouter()     #its custamisable router changes can apply
router.register('task',TaskViewset)
router.register('completed_task',views.Completed)
router.register('due_task',views.DueTaskViewset)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('register/', views.CreateuserView.as_view(), name='user'),

    path('api_auth/', include('rest_framework.urls')),

    path('', include(router.urls)),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
