from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('accounts.urls')),
    path('divulgar/', include('divulge.urls')),
    path('adotar/', include('adopt.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
