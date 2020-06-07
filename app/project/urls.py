from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


from upload.views import image_upload, index
from .serializer import router

urlpatterns = [
    path('', index, name="index"),
    path('upload', image_upload, name="upload"),

    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path("ACP/", admin.site.urls),

    # API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
