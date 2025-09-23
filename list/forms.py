from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ['content', 'optional_deadline_datetime', 'tags']
        widgets = {
            'optional_deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
