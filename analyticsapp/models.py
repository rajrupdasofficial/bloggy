from django.db import models

# Create your models here.

class Analytics(models.Model):
    ip = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f"{self.ip}"

    class Meta:
        verbose_name = 'Analytic'
        verbose_name_plural = 'Analytics'