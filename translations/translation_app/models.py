from django.db import models

# Create your models here.
class TextEntry (models.Model):
    english_text = models.TextField()
    french_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.english_text[:50] #Display first 50 characters