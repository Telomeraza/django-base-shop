
from django.contrib import admin
from django.urls import path, include   # 18.
from django.conf import settings   # 26.
from django.conf.urls.static import static   # 27.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),  # 19.
    path('cart/', include('cart.urls', namespace='cart')),  # 39.
]

# 25.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
