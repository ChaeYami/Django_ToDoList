from django.urls import path,include
from todoapp import views


urlpatterns = [
    path('',views.ToDoView.as_view(), name="todo_view"), # /todo/
    path('<int:todo_id>/', views.ToDoDetailView.as_view(),name="todo_detail_view") # /todo/id/

]