# Generated by Django 4.0.6 on 2022-08-11 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Time', models.TimeField(null=True)),
                ('Desc', models.TextField(null=True)),
            ],
        ),
    ]
