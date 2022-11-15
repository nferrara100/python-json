from django.db import models


class FreeText(models.Model):
    text = models.TextField(blank=False, null=False, max_length=256)
