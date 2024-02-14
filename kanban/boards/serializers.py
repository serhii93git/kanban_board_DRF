from rest_framework import serializers
from .models import *
from users.serializers import *


class NotesSerializer(serializers.ModelSerializer):
    """Serializer for Notes model"""

    class Meta:
        model = Notes
        fields = '__all__'


class TaskAboutSerializer(serializers.ModelSerializer):
    """Serializer for TaskAbout model"""

    class Meta:
        model = TaskAbout
        fields = '__all__'


class TaskStatusSerializer(serializers.ModelSerializer):
    """Serializer for TaskStatus model"""

    class Meta:
        model = TaskStatus
        fields = '__all__'


class SubtaskSerializer(serializers.ModelSerializer):
    """Serializer for SubtaskStatus model"""

    class Meta:
        model = Subtask
        fields = "__all__"


class PrimaryTaskSerializer(serializers.ModelSerializer):
    """Serializer for PrimaryTask model"""

    class Meta:
        model = PrimaryTask
        fields = "__all__"


class NestedSubtaskSerializer(serializers.ModelSerializer):
    """Nested Serializer for Subtask model to use in MainBoard Serializer"""

    class Meta:
        model = Subtask
        fields = ['id', 'title', 'status']


class NestedTaskAboutSerializer(serializers.ModelSerializer):
    """Serializer for TaskAbout model"""

    class Meta:
        model = TaskAbout
        fields = '__all__'


class NestedTaskStatusSerializer(serializers.ModelSerializer):
    """Nested Serializer for TaskStatus model to use in MainBoard Serializer"""

    class Meta:
        model = TaskStatus
        fields = ['title', ]


class NestedPrimaryTaskSerializer(serializers.ModelSerializer):
    """Nested Serializer for PrimaryTask model to use in MainBoard Serializer"""
    subtasks = NestedSubtaskSerializer(many=True)
    task_about = NestedTaskAboutSerializer(many=True)
    status = NestedTaskStatusSerializer()

    class Meta:
        model = PrimaryTask
        fields = "__all__"


class MainBoardSerializer(serializers.ModelSerializer):
    """Serializer for MainBoard model"""
    task = NestedPrimaryTaskSerializer()
    author = AuthorSerializer()

    class Meta:
        model = MainBoard
        fields = '__all__'
