DEFAULT_SUPERUSER_EMAIL = "foo@foo.com"
DEFAULT_SUPERUSER_PASSWORD = "foo"

from django.db import migrations
from django.contrib.auth.models import User


def forwards_func(apps, schema_editor):
    User.objects.create_superuser(
        username=DEFAULT_SUPERUSER_EMAIL,
        password=DEFAULT_SUPERUSER_PASSWORD,
    )


def remove_user(apps, schema_editor):
    User.objects.get(username=DEFAULT_SUPERUSER_EMAIL).delete()


class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.RunPython(forwards_func, remove_user),
    ]
