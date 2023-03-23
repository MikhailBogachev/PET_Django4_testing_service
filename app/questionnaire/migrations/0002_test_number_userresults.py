# Generated by Django 4.1.7 on 2023-03-18 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_correct_answer', models.IntegerField()),
                ('set_of_tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.setoftests')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]