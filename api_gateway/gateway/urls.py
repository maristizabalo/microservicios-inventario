from django.urls import path
from .views import ProxyView

urlpatterns = [
    path('<str:service>/<path:path>', ProxyView.as_view()),
]
