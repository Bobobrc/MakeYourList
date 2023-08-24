# Generated by Django 4.2.4 on 2023-08-24 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50, unique=True)),
                ('list_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('important', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MakeList.list')),
            ],
        ),
    ]
