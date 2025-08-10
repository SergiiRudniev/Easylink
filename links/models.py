from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()


def generate_slug():
    return get_random_string(6)


class LinkGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Domain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Pixel(models.Model):
    GA = "ga"
    FB = "fb"
    SERVICE_CHOICES = [
        (GA, "Google Analytics"),
        (FB, "Facebook"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    code = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} - {self.service}"


class ShortLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20, unique=True, default=generate_slug)
    original_url = models.URLField()
    group = models.ForeignKey(LinkGroup, null=True, blank=True, on_delete=models.SET_NULL)
    domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.SET_NULL)
    pixel = models.ForeignKey(Pixel, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.slug


class Click(models.Model):
    link = models.ForeignKey(ShortLink, related_name="clicks", on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=256)
    referer = models.CharField(max_length=256, blank=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self) -> str:
        return f"{self.link.slug} @ {self.clicked_at}"
