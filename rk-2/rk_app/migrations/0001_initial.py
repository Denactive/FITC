# Generated by Django 2.2.25 on 2021-12-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('format', models.TextField()),
                ('size', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'диск',
                'verbose_name_plural': 'диски',
                'db_table': 'Disks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=80)),
                ('fk_storedDisks', models.ManyToManyField(to='rk_app.Disk')),
            ],
            options={
                'verbose_name': 'библиотека',
                'verbose_name_plural': 'библиотеки',
                'db_table': 'Libraries',
                'managed': True,
            },
        ),
    ]
