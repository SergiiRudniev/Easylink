from django.contrib import admin
from .models import LinkGroup, Domain, Pixel, ShortLink, Click


@admin.register(LinkGroup)
class LinkGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "user")


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "verified")


@admin.register(Pixel)
class PixelAdmin(admin.ModelAdmin):
    list_display = ("user", "service")


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ("slug", "user", "original_url", "created_at")
    search_fields = ("slug", "original_url")


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ("link", "clicked_at", "ip_address")
    list_filter = ("clicked_at",)
