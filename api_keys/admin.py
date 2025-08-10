from django.contrib import admin
from .models import APIKey

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ["user", "key", "created_at"]
    search_fields = ["user__username", "key"]
