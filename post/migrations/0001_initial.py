# Generated by Django 2.2.6 on 2019-12-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authorpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField(default='Tutorial Content')),
                ('date_published', models.DateField(blank=True, null=True)),
                ('user_profile_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
