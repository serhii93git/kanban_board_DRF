from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MainBoard)
admin.site.register(PrimaryTask)
admin.site.register(Subtask)
admin.site.register(Notes)
admin.site.register(TaskAbout)
admin.site.register(TaskStatus)

