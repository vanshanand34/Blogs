from django.urls import path 
from . import views 

urlpatterns = [
    path('posts/',views.index,name='index'),
    path('posts/<int:pk>',views.mypost,name='mypost'),
    path('posts/create/',views.create,name='create')
]