# Generated by Django 3.0.6 on 2020-05-08 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200506_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Выполнено'),
        ),
    ]
