from django.contrib import admin
from django.urls import path
from restaurante.views import index, cardapio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('cardapio',cardapio, name='cardapio'),
] + static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)


 