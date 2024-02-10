from django.db import models


class TaskStatus(models.Model):
    """A model for creating an unlimited number of custom task statuses"""

    title = models.CharField(max_length=50, verbose_name='task status title',
                             help_text='the status of the task. for example: to do, completed, etc')

    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='subtask author')

    def __str__(self):
        return self.title


class TaskAbout(models.Model):
    """A model for creating an unlimited number of explanations and additional materials for tasks"""

    title = models.CharField(max_length=100, verbose_name='explanation title')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='create time',
                                       help_text='explanation create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='update time',
                                       help_text='explanation last change time')
    files = models.FileField(upload_to='files/', null=True, blank=True, verbose_name='files storage',
                             help_text='files for additional explanation')  # to do: add size/type validators

    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='explanation author')

    def __str__(self):
        return self.title


class Subtask(models.Model):
    """A model for creating an unlimited number of subtasks"""

    title = models.CharField(max_length=50, verbose_name='title', help_text='subtask title')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='create time', help_text='subtask create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='update time', help_text='subtask last change time')
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='subtask author')
    status = models.BooleanField(default=False, verbose_name='subtask status',
                                 help_text='if subtask done - True, if not - False')

    def __str__(self):
        return self.title


class PrimaryTask(models.Model):
    # to do: signal for automatic primary task status check. If all subtask done - PT done to
    """A model for creating an unlimited number of primary tasks"""

    title = models.CharField(max_length=50, verbose_name='title', help_text='primary task title')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='create time',
                                       help_text='primary task create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='update time',
                                       help_text='primary task last change time')
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='primary task author')
    subtask = models.ForeignKey(to=Subtask, on_delete=models.PROTECT, verbose_name='subtask',
                                help_text='subtask for primary task')
    status = models.ForeignKey(to=TaskStatus, on_delete=models.CASCADE, verbose_name='primary task status',
                               help_text='for example: to do, completed, etc')

    def __str__(self):
        return self.title


class MainBoard(models.Model):
    """A model for main page board"""

    title = models.CharField(max_length=50, verbose_name='main board title', help_text='name your project')
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='project author')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='create time', help_text='note create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='update time', help_text='note last change time')
    task = models.ForeignKey(to=PrimaryTask, on_delete=models.CASCADE, verbose_name='primary tasks',
                             help_text='primary tasks for main board')

    def __str__(self):
        return self.title


class Notes(models.Model):
    """A model for creating an unlimited number of notes"""

    title = models.CharField(max_length=50, verbose_name='notes title', help_text='Add title for your note')
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='note author')
    text = models.TextField(verbose_name='note text', help_text='Add text for your note')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='create time', help_text='note create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='update time', help_text='note last change time')
    files = models.FileField(upload_to='files/', null=True, blank=True, verbose_name='files storage',
                             help_text='files for additional explanation')  # to do: add size/type validators

    def __str__(self):
        return self.title
