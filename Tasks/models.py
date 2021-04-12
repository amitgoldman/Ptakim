from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="task_owner")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="execute_user")

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()
