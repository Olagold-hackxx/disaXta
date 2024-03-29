# Generated by Django 5.0 on 2024-03-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_follower_options_alter_following_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_text',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d'),
        ),
    ]
