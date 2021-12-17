from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note', views.note, name='note'),
    path('setting', views.setting, name='setting'),
    path('note/save', views.save_note, name='save_note'),
    path('note/delete/<int:id>', views.delete_note, name='delete_note')
]