from django.contrib.auth import logout, login
from django.urls import path

from medical.views import medical_view, delete_medicine, add_medicine, update_view, logoutUser

urlpatterns = [
    path('', medical_view, name='medical'),
    path('logoutUser', logoutUser, name='logout'),
    path('login', login, name='login'),
    path('delete/<int:pk>/', delete_medicine, name='delete_medicine'),
    path('add/', add_medicine, name='add_medicine'),
    path('update/<int:pk>/', update_view, name='update_view'),
]
