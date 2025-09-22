from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from list.models import Tag, Task


def index(request) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_visits": num_visits + 1
    }
    return render(request, "list/index.html", context=context)


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 10

class TagsListView(ListView):
    model = Tag
    context_object_name = "tags"
    paginate_by = 10
    template_name = "list/tags_list.html"

