# Generated by Django 2.1.3 on 2018-12-27 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_emailconfirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='hashkey',
            new_name='activation_key',
        ),
    ]
