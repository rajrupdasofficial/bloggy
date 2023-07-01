from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    subject = models.CharField(max_length=255, default=None, blank=True, null=True)
    message = models.TextField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"contact name {self.name}, contact name {self.email}"

    class Meta:
        ordering = ['-created']
