from django.urls import path


from list.views import(index,
TagsListView,
TagsCreateView,
TagsUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tags-update"),
]

app_name = "list"