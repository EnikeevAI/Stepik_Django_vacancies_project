# Generated by Django 3.0.5 on 2020-05-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_auto_20200523_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_cover_letter',
            field=models.CharField(max_length=500),
        ),
    ]
