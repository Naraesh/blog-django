# Generated by Django 2.2.6 on 2019-12-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20191221_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorpost',
            name='user_profile_link',
            field=models.TextField(max_length=200),
        ),
    ]
