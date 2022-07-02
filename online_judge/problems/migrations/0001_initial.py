# Generated by Django 4.0.5 on 2022-07-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=20)),
                ('question_desc', models.TextField(max_length=250)),
                ('difficulty', models.TextField(max_length=10)),
                ('time_limit', models.IntegerField(default=1000)),
                ('input_format', models.TextField(max_length=50)),
                ('output_format', models.TextField(max_length=50)),
            ],
        ),
    ]