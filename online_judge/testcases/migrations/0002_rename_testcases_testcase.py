# Generated by Django 4.0.5 on 2022-07-02 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_status_alter_problem_difficulty_and_more'),
        ('testcases', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testcases',
            new_name='Testcase',
        ),
    ]
