from django.contrib import admin
from django.urls import path
from core.views import LandingPageView
from todos import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing'),
    path('todos/', todo_views.todo_list, name='todo_list'),
    path('todos/reorder/', todo_views.reorder_tasks, name='reorder_tasks'),
]
