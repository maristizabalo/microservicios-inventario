from django.contrib import admin
from django.urls import path, include
from gateway.urls import urlpatterns as gateway_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(gateway_urls)),
]
