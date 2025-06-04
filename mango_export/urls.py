from django.contrib import admin
from django.urls import path
from views import mango_list, mango_create, mango_update, mango_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mango_list, name='mango_list'),
    path('create/', mango_create, name='mango_create'),
    path('update/<int:pk>/', mango_update, name='mango_update'),
    path('delete/<int:pk>/', mango_delete, name='mango_delete'),
]