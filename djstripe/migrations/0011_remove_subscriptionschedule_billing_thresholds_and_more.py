# Generated by Django 4.0.1 on 2022-01-12 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0010_alter_customer_balance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscriptionschedule",
            name="billing_thresholds",
        ),
    ]
