# Generated by Django 2.1.3 on 2018-12-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181204_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image_link',
            field=models.CharField(default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png', max_length=500),
        ),
    ]
