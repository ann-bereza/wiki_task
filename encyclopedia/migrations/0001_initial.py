# Generated by Django 3.2.8 on 2021-10-27 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Content', models.TextField(max_length=256)),
            ],
        ),
    ]
