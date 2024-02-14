from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


class TaskStatusView(ModelViewSet):
    """View for TaskStatus Serializer"""

    serializer_class = TaskStatusSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return TaskStatus.objects.filter(author=self.request.user)


class SubtaskView(ModelViewSet):
    """View for Subtask Serializer"""

    serializer_class = SubtaskSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Subtask.objects.filter(author=self.request.user)


class PrimaryTaskView(ModelViewSet):
    """View for PrimaryTask Serializer"""

    serializer_class = PrimaryTaskSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return PrimaryTask.objects.filter(author=self.request.user)

class TaskAboutView(ModelViewSet):
    """View for TaskAbout Serializer"""

    serializer_class = TaskAboutSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return TaskAbout.objects.filter(author=self.request.user)

class MainBoardView(ReadOnlyModelViewSet):
    """View for MainBoard Serializer"""

    serializer_class = MainBoardSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return MainBoard.objects.filter(author=self.request.user)


class NotesView(ModelViewSet):
    """View for Notes Serializer"""
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)
