import self
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView

from list.forms import TaskForm
from list.models import Tag, Task


class ToggleTaskStatusView(generic.UpdateView):
    model = Task
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.boolean_field = not task.boolean_field
        task.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("list:task-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "list/index.html"
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")
    template_name = "list/task_confirm_delete.html"


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    paginate_by = 10
    template_name = "list/tags_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tags-list")
    template_name = "list/tag_form.html"


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tags-list")
    template_name = "list/tag_form.html"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tags-list")
    template_name = "list/tag_confirm_delete.html"
