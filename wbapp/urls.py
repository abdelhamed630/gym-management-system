from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('dashbord',views.dashbord,name="dashbord"),
    path('logout',views.logout,name="logout"),
    path("record",views.creat_record,name='record'),
    path('view/<int:record_id>/',views.view,name="view"),
    path('update_record/<int:record_id>/',views.update_record,name="update_record"),
    path('daelet/<int:record_id>/',views.delete,name="delete"),
    path('search',views.search,name="search"),
    path("renew_payment/<int:record_id>/", views.renew_payment, name="renew_payment"),
    ]
