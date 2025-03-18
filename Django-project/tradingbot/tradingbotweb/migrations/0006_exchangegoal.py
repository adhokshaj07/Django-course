# Generated by Django 5.1.7 on 2025-03-16 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbotweb', '0005_alter_currencybalance_share_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('executed_at', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('destination_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange_goal', to='tradingbotweb.currency')),
                ('origin_balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange_goal', to='tradingbotweb.currencybalance')),
                ('transaction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tradingbotweb.transaction')),
            ],
        ),
    ]
