from django.contrib import admin
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework import status, serializers, views
from django.conf.urls import url, include
from caesar_cipher import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', csrf_exempt(views.CaesarCipherView.as_view()), name='create')
]
