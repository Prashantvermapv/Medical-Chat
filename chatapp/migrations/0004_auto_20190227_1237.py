# Generated by Django 2.0.7 on 2019-02-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_suggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='sug1',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='sug2',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='sug3',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='sug4',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]