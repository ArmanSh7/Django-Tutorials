# Generated by Django 3.1.5 on 2021-03-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210319_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='intsrests',
            new_name='interests',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
