from django.urls import path

from . import views

app_name = 'kipos'
urlpatterns = [
    path('main', views.MainView.as_view(), name = 'main'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('allmodules', views.allmodules,name='modulelist'),
    path('addmodule',views.addmodule,name='addmodule')
]
