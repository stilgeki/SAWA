# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_input', models.FileField(upload_to='', verbose_name='data/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_text', models.CharField(blank=True, max_length=5000, null=True)),
                ('created_date', models.CharField(blank=True, max_length=25, null=True)),
                ('rating', models.IntegerField()),
                ('activity_name', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terrible_sentiment', models.FloatField()),
                ('bad_sentiment', models.FloatField()),
                ('neutral_sentiment', models.FloatField()),
                ('good_sentiment', models.FloatField()),
                ('excellent_sentiment', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SentimentPercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_terrible', models.FloatField()),
                ('pt_bad', models.FloatField()),
                ('pt_neutral', models.FloatField()),
                ('pt_good', models.FloatField()),
                ('pt_excellent', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaOutreach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.IntegerField()),
                ('twitter', models.IntegerField()),
                ('offline', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='outreach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sawa.SocialMediaOutreach'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sawa.ReviewUser'),
        ),
        migrations.AddField(
            model_name='fileinput',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sawa.Review'),
        ),
        migrations.AddField(
            model_name='fileinput',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sawa.ReviewUser'),
        ),
        migrations.AddField(
            model_name='fileinput',
            name='smoutreach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sawa.SocialMediaOutreach'),
        ),
    ]
