from django.db import migrations
from django.contrib.auth.models import Group


def create_club_admin_group(apps, schema_editor):
    Group.objects.get_or_create(name='club_admin')


class Migration(migrations.Migration):
    dependencies = [
        ('unihub', '0003_create_club_member_group'),
    ]

    operations = [
        migrations.RunPython(create_club_admin_group),
    ]
