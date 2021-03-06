# Generated by Django 3.0.8 on 2020-07-25 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(upload_to='tech/')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('sub_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.SubTopics')),
            ],
        ),
        migrations.AddField(
            model_name='subtopics',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Technology'),
        ),
    ]
