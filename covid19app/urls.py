from django.contrib import admin
from django.urls import path
from .views import index,country

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('/<slug:country>',country)
]
