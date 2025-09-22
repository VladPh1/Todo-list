from django.urls import path


from list.views import(index,
TagsListView,
TagsCreateView,
TagsUpdateView,
TagsDeleteView,
TaskListView,
TaskCreateView,
TaskUpdateView,
TaskDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete", TagsDeleteView.as_view(), name="tags-delete"),
    path("task/", TaskListView.as_view(), name="task"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "list"