from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title="Test Task", description="Task Description")

    def test_task_creation(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.title, "Test Task")
