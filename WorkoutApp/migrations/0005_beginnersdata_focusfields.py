# Generated by Django 5.0.2 on 2024-02-22 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutApp', '0004_rename_beginner_beginnersdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='beginnersdata',
            name='FocusFields',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
