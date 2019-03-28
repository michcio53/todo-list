from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView)

from tasks.models import Task
from tasks.serializers.task import (ListTaskSerializer,
                                    TaskSerializer,
                                    UpdateTaskSerializer)

from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from core.permissions import IsOwnerOrRead


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ListTaskSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']  # to use filter use /tasks/?search=message


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUserListView(ListAPIView):
    serializer_class = ListTaskSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Task.objects.filter(user=self.request.user)
        return queryset_list


class TaskDetailsView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = ListTaskSerializer


class TaskUpdateStatusView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = UpdateTaskSerializer
    permission_classes = (IsOwnerOrRead, )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


