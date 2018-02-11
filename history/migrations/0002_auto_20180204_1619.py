# Generated by Django 2.0.2 on 2018-02-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='created_time',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='subject',
            name='update_date',
            field=models.DateTimeField(default='2018-02-04'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='history_rating',
            field=models.CharField(max_length=1000),
        ),
    ]