from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from .models import Profile


def profile_created(sender, instance, created, **kwargs):
    print("signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def profile_deleted(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
        print("User deleted")
    except:
        pass


post_save.connect(profile_created, sender=User)
post_delete.connect(profile_deleted, sender=Profile)
