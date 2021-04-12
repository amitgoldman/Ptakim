from django.db import models
from django.contrib.auth import get_user_model


class TaskList(models.Model):
    title = models.CharField(max_length=32)

    menger = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="task_list_menger")

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Task(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    assigner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="task_owner")
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="task_list")

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_list}'s {self.title}"

    def __repr__(self):
        return self.__str__()

