from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('acounts/', include('acounts.urls')),
                  path('blog/', include("veblog.urls")),
                  path('coach/', include('coach.urls')),
                  path('course/', include('course.urls')),
                  path('massage/', include('massage.urls')),
                  path('hesabdari/', include('hesabdari.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
