from django.urls import path

from apps.puls_prodaj_test.views.calculate_proxy_server import calculate_proxy_server
from apps.puls_prodaj_test.views.external_proxy import external_proxy

urlpatterns = [
    path('v1/skills', external_proxy, name='proxy-list'),
    path('v1/skills/<str:uuid>', external_proxy, name='proxy-detail'),
    path('proxy_address', calculate_proxy_server, name='proxy-address'),
]
