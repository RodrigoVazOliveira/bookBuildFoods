import django.contrib
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('recipe.urls')),
    path('users/', include('apps.users.urls')),
    path('admin/', django.contrib.admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)