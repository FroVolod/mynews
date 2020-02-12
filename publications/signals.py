from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from publications.models import Publication, Comment

from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def u(sender, request, user, **kwargs):
    user.groups.add(Group.objects.get(name='users'))
