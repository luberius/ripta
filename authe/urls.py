from django.urls import include, path

from authe import views

urlpatterns = [
    path('login', views.index, name='login'),
    path('do_login', views.do_login, name='do_login'),
    path('logout', views.do_logout, name='do_logout')
]
