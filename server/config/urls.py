from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.puls_prodaj_test.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [
                      path('api-auth/', include('rest_framework.urls')),
                      path('docs/', get_swagger_view(title='Pastebin API')),
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
