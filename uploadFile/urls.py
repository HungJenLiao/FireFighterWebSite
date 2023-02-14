from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login, name = 'login'), 
    path('accounts/logout/', views.logout, name = 'logout'), 
    path('uploadFile/', views.uploadFile, name = 'uploadfile'), 
    path('dashboard/', views.dashboard, name = 'dashboard'), 
    path('dashboard_model/', views.dashboard_model), 
    path('emergency_list/', views.emergency_list, name = 'EmList'), 
    path('emergency_list/update/<int:Em_id>/', views.emergency_list_update, name = 'EmListUpdate'),
    path('emergency_list/edit/', views.emergency_list_edit, name = 'EmListEdit'),
    path('test/', views.test), 
    path('member_list/', views.member_list, name = 'MemberList'), 
    path('logrecord_list/', views.logrecord_list, name = 'LogList'), 
    path('news/', views.news, name = 'news')
]