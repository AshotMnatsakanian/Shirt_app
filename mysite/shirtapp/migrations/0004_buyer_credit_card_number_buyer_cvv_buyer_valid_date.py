# Generated by Django 4.2.5 on 2023-10-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtapp', '0003_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='credit_card_number',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='buyer',
            name='cvv',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='buyer',
            name='valid_date',
            field=models.CharField(default='', max_length=4),
        ),
    ]
