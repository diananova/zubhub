# Generated by Django 2.2.7 on 2020-12-02 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.Project'),
        ),
    ]
