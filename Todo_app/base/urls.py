from django.urls import path
from . import views
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<str:pk>/',TaskDetail.as_view(),name='task'),
    path('create-task/',TaskCreate.as_view(),name='task-create'),
    path('update-task/<str:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('delete-task/<str:pk>/',TaskDelete.as_view(),name='task-delete'),
    
    path('login/',CustomLoginView.as_view(),name='task-login'),
    path('logout/',LogoutView.as_view(next_page='Login'),name='task-logout'),
    path('register/',RegisterPage.as_view(),name='register')
    
]
