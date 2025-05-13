from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        help_text="The name of the tag"
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"


    title = models.CharField(
        max_length=255,
        help_text="The title of the task"
    )
    description = models.TextField(
        blank=True,
        help_text="Description of the task"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        help_text="Current status of the task"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time the task was created"
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True,
        help_text="Tags related to the task"
    )


    def __str__(self):
        return f"[{self.title}] {self.status}"
