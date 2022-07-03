# Generated by Django 4.0.5 on 2022-07-03 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0002_problem_status_alter_problem_difficulty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='c++', max_length=20)),
                ('code', models.TextField()),
                ('status', models.CharField(max_length=10)),
                ('question_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
