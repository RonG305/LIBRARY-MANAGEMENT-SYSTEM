from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_books/', views.add_books, name='add_books'),
    path('update/<str:pk>', views.update_books, name='update'),
     path('delete/<str:pk>', views.delete_books, name='delete')
]
    