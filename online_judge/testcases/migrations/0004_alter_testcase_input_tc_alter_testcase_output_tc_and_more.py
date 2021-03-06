# Generated by Django 4.0.5 on 2022-07-03 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_status_alter_problem_difficulty_and_more'),
        ('testcases', '0003_alter_testcase_input_tc_alter_testcase_output_tc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='input_tc',
            field=models.FileField(default=None, max_length=250, upload_to='<django.db.models.fields.related.OneToOneField>/input/'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='output_tc',
            field=models.FileField(default=None, max_length=250, upload_to='<django.db.models.fields.related.OneToOneField>/output/'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='question_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problems.problem'),
        ),
    ]
