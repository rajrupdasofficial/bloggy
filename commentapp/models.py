from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    comment = models.TextField(null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"comment author name {self.name}, comment author email {self.email}"

    class Meta:
        ordering = ['-created']