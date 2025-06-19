from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('applications/', include('applications.urls')),
    path('projects/', include('projects.urls')),
    path('media/', include('media.urls')),
    path('flashcards/', include('flashcards.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('applications/', include('applications.urls')),
    path('projects/', include('projects.urls')),
    path('media/', include('media.urls')),
    path('flashcards/', include('flashcards.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)