# Generated by Django 3.2.5 on 2021-11-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_oldhandles'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldhandles',
            name='name',
            field=models.CharField(default='deland', max_length=200),
            preserve_default=False,
        ),
    ]