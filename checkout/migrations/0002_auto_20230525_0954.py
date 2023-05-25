# Generated by Django 3.2.19 on 2023-05-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address',
            new_name='street_address1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
