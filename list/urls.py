from django.urls import path


from list.views import(index,
TagsListView,
TagsCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create", TagsCreateView.as_view(), name="tags-create"),
]

app_name = "list"