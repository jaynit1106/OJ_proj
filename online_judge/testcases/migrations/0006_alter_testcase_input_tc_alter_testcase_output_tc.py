# Generated by Django 4.0.5 on 2022-07-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0005_alter_testcase_input_tc_alter_testcase_output_tc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='input_tc',
            field=models.FileField(default=None, max_length=250, upload_to='input/'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='output_tc',
            field=models.FileField(default=None, max_length=250, upload_to='output/'),
        ),
    ]
