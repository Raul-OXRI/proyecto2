from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender=Usuario)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            group, created = Group.objects.get_or_create(name='Admin')
            instance.groups.add(group)
        elif instance.role == 'employee':
            group, created = Group.objects.get_or_create(name='Employee')
            instance.groups.add(group)
        elif instance.role == 'client':
            group, created = Group.objects.get_or_create(name='Client')
            instance.groups.add(group)
