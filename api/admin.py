from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ["id", "email", "content", "created"]
