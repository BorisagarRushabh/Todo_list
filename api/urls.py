from django.urls import path
from . import views

urlpatterns =[
    path("readAll/", views.getAllTask),
    path("readOne/", views.getOneTask),
    path("createTask/", views.addNewTask),
    path("updateTask/<int:pk>",views.updateTask)
]
