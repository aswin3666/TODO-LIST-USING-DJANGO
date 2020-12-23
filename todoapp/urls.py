from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('submit',views.submit,name="submit"),
    path('submit/update/<int:todo_id>/',views.update,name="update"),
    path('submit/delete/<int:todo_id>/',views.delete,name="delete"),
]