# Generated by Django 3.0.4 on 2020-07-25 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseplants', '0002_plant_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='chinese_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='comfortable_temp',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='date_purchased',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='english_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='family',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='full_sun',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='half_sun',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='max_temp',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='min_temp',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='scientific_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='shadow',
        ),
    ]