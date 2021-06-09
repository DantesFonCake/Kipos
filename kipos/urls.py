from django.urls import path

from . import views

app_name = 'kipos'
urlpatterns = [
    path('main', views.MainView.as_view(), name = 'main'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('allmodules', views.allmodules,name='modulelist'),
    path('addmodule',views.addmodule,name='addmodule'),
    path('module/update',views.update,name='update'),
    path('connection_check',views.check_connection,name='connection_check'),
    path('module/delete',views.deletemodule,name='deletemodule'),
]
