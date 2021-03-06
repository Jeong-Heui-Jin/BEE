# Generated by Django 3.2.3 on 2021-09-23 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('corporates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corporate',
            name='scrap_user',
        ),
        migrations.AddField(
            model_name='corporate',
            name='scrap_user',
            field=models.ManyToManyField(related_name='scrap_corporates', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_term', models.FloatField()),
                ('term_ratio', models.FloatField()),
                ('news_score', models.FloatField()),
                ('news_cnt', models.IntegerField()),
                ('corporate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporates.corporate')),
            ],
        ),
        migrations.CreateModel(
            name='Governance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_ration', models.FloatField()),
                ('board_independency', models.BooleanField()),
                ('salary_gap', models.FloatField()),
                ('dividen_ratio', models.FloatField()),
                ('largest_shareholder', models.FloatField()),
                ('news_score', models.FloatField()),
                ('news_cnt', models.IntegerField()),
                ('corporate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporates.corporate')),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2', models.IntegerField()),
                ('energy', models.IntegerField()),
                ('news_score', models.FloatField()),
                ('news_cnt', models.IntegerField()),
                ('corporate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporates.corporate')),
            ],
        ),
    ]
