from django.urls import path
from . import views
from .views import  esewa_payment_view
from .views import esewa_success, esewa_failure

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('esewa/payment/<int:book_id>/', views.esewa_payment_view, name='esewa_payment'),

    path('esewa/success/', esewa_success, name='esewa_success'),
    path('esewa/failure/', esewa_failure, name='esewa_failure'),
]
