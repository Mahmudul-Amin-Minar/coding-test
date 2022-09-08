from statistics import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .utils import create_shortcode
from .validators import validate_url

# Create your models here.

User = get_user_model()

class ShortenUrl(models.Model):
    url = models.TextField(validators=[validate_url])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        
        super(ShortenUrl, self).save(*args, **kwargs)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode})
        return "http://127.0.0.1:8000" + url_path