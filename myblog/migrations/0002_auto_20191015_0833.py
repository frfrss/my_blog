# Generated by Django 2.2.3 on 2019-10-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(default='', max_length=32),
        ),
    ]
