from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login, name = 'login'), 
    path('accounts/logout/', views.logout, name = 'logout'), 
    path('uploadFile/', views.uploadFile), 
    path('dashboard/', views.dashboard), 
    path('dashboard_model/', views.dashboard_model), 
    path('emergency_list/', views.emergency_list), 
    path('emergency_list/edit/<int:id>/', views.emergency_list_edit),
    path('test/', views.test), 
    path('member_list/', views.member_list), 
    path('logrecord_list/', views.logrecord_list), 
    path('news/', views.news)
]