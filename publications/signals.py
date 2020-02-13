from django.dispatch import receiver
from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def user_add_group(sender, request, user, **kwargs):
    user.groups.add(Group.objects.get(name='users'))
