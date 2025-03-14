from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='cities'),
    path('<str:city_name>/', views.detail, name='city'),
    path('add', views.add_city, name='add_city'),
    path('<str:city_name>/delete', views.delete_city, name='delete_city'),
    path('weathers', views.weathers_data, name='weathers_data'),
    path('<str:city_name>/update/', views.update_city, name='update_city'),
]