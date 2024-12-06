from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'timestamp')
    search_fields = ('title', 'tags')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
    )
