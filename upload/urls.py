from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
    path('api/upload/', views.upload_image_api, name='upload_image_api'),
]
