# Generated by Django 5.0.2 on 2024-02-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutApp', '0006_beginnerschest_rename_beginnersdata_beginnersabs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beginnerschest',
            name='FocusFields',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
