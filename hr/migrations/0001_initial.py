# Generated by Django 2.2.2 on 2019-11-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('profile', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
