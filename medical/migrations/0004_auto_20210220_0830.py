# Generated by Django 3.1.6 on 2021-02-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0003_auto_20210220_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalstore',
            name='expired_date',
            field=models.DateField(),
        ),
    ]
