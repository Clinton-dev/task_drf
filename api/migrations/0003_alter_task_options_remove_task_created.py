# Generated by Django 4.0.6 on 2022-07-18 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_task_options_task_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]