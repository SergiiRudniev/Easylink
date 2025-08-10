from django.contrib import admin

from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "subject", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("subject", "message", "user__username")
    readonly_fields = ("created_at", "updated_at")
