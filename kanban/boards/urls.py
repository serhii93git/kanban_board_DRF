from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register(r'notes', NotesView, basename='notes')
router.register(r'main', MainBoardView, basename='main-board')
router.register(r'primary-task', PrimaryTaskView, basename='primary-task')
router.register(r'subtask', SubtaskView, basename='subtask')
router.register(r'task-status', TaskStatusView, basename='task-status')
router.register(r'task-about', TaskAboutView, basename='task-about')


urlpatterns = router.urls

