# Generated by Django 2.2.6 on 2019-10-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTime', '0002_auto_20191018_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws_b',
            name='Answer',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='redhat_b',
            name='Answer',
            field=models.CharField(max_length=5),
        ),
    ]
