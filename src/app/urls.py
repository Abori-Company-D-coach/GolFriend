from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
# #from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('board.urls'))
# ]

# urlpatterns += staticfiles_urlpatterns()