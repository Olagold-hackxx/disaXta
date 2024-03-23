# Generated by Django 5.0 on 2024-03-23 02:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_follower_options_follower_created_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomToken',
            new_name='Token',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='comment',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='savers',
            field=models.ManyToManyField(blank=True, related_name='saved_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
