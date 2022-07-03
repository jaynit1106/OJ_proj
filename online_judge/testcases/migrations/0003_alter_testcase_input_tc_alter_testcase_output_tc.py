# Generated by Django 4.0.5 on 2022-07-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0002_rename_testcases_testcase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='input_tc',
            field=models.FileField(default=None, max_length=250, upload_to='<django.db.models.fields.related.ForeignKey>/input/'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='output_tc',
            field=models.FileField(default=None, max_length=250, upload_to='<django.db.models.fields.related.ForeignKey>/output/'),
        ),
    ]
