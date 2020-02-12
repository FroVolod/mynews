from django.db import migrations
from django.contrib.auth.management import create_permissions

def create_user_groups(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    GROUPS = ['admins', 'editors', 'users']

    for group in GROUPS:
        new_group = Group.objects.create(name=group)
        if group == 'users':
            continue
        model_add_perm = Permission.objects.get(name='Can change publication')
        new_group.permissions.add(model_add_perm)


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_user_groups),
    ]
