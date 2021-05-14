# Generated by Django 2.2.7 on 2020-12-10 01:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0016_auto_20201202_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creator',
            name='followers_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='creator',
            name='projects_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
