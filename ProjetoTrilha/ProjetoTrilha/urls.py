from django.contrib import admin
from django.urls import path, include
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='url_home'),
    path('homeFunc', homeFunc, name='url_HomeFunc'),
    path('novo', add_apartamento, name='url_novoApartamento'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
]
