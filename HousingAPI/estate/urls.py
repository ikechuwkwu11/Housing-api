from django.urls import path
from .views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'house', HouseView, basename='house')

urlpatterns = [
    path('', include(router.urls)),
    path('register/',Register.as_view(),name = 'Register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('add-house/',AddHouse.as_view(),name='add-House'),
    path('edit-house/<int:house_id>',EditHouse.as_view(),name='edit-house'),
    path('delete-house/<int:house_id>',DeleteHouse.as_view(),name ='delete-house')
]