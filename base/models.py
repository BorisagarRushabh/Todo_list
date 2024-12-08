from django.db import models
from django.core.exceptions import ValidationError


class Status(models.TextChoices):
    ACTIVE = "A", "Open"
    INACTIVE = "I", "Working"
    PENDING = "P", "Pending Work"
    COMPLETED = "C", "Completed"
    OVERDUE = "O", "Overdue"
    CANCELLED = "X", "Cancelled"


class Task(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100, null=False)
    Description = models.CharField(max_length=1000, null=False)
    dueDate = models.DateField(null=True)
    # Tag = models.enums() //ask rushabh about this one
    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.PENDING, null=False
    )

    def dueDateValidation(self):
        if self.timeStamp >= self.dueDate:
            raise ValidationError("Due Date cannot be less than created date")
