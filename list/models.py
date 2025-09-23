from django.db import models

class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    optional_deadline_datetime = models.DateTimeField(blank=True, null=True)
    boolean_field = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['boolean_field', '-datetime']


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
