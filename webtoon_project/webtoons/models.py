from django.db import models
import json

class Webtoon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    characters = models.TextField()  # Changed from JSONField to TextField

    def set_characters(self, characters):
        self.characters = json.dumps(characters)

    def get_characters(self):
        return json.loads(self.characters)

    def __str__(self):
        return self.title
