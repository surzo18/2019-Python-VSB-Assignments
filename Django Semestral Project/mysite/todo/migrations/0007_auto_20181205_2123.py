# Generated by Django 2.1.3 on 2018-12-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20181205_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image_link1',
            field=models.CharField(default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png', max_length=50),
        ),
        migrations.AlterField(
            model_name='film',
            name='image_link2',
            field=models.CharField(default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png', max_length=50),
        ),
        migrations.AlterField(
            model_name='film',
            name='image_link3',
            field=models.CharField(default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png', max_length=50),
        ),
    ]
