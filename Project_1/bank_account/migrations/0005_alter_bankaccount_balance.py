# Generated by Django 5.0.7 on 2024-08-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0004_alter_bankaccount_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.PositiveBigIntegerField(),
        ),
    ]
