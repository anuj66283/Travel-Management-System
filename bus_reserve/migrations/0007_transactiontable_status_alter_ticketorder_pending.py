# Generated by Django 5.0.1 on 2024-01-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_reserve', '0006_transactiontable_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiontable',
            name='status',
            field=models.CharField(choices=[('1', 'Completed'), ('2', 'Pending'), ('3', 'Refunded')], default='2', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='pending',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
