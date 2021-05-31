from django.db import models


class Article(models.Model):
    text = models.TextField(
        verbose_name="Text"
    )
    category = models.CharField(
        max_length=128,
        verbose_name="Category"
    )

    def __str__(self):
        return f"{self.text[:20]} ..."
