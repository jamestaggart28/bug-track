# Generated by Django 2.0.2 on 2018-03-07 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='name',
            field=models.CharField(default='Test Bug', max_length=30),
            preserve_default=False,
        ),
    ]
