from profileapp.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()
print(User)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("def section working")
    if created:
        print("if created working")
        UserProfile.objects.create(user=instance)