from .api.task import (TaskListView,
                       TaskCreateView,
                       TaskUserListView,
                       TaskDetailsView,
                       TaskUpdateStatusView,)

from django.urls import path

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),  # Index & Search
    path('create/', TaskCreateView.as_view(), name='create'),  # Create new task
    path('user-tasks/', TaskUserListView.as_view(), name='user-tasks'),  # My Tasks
    path('details/<int:pk>', TaskDetailsView.as_view(), name='details'),  # Task details
    path('status-update/<int:pk>', TaskUpdateStatusView.as_view(), name='status-update')  # Change task status
]
