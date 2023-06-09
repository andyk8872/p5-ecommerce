# Generated by Django 3.2.19 on 2023-06-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=700)),
                ('subject', models.CharField(choices=[('general', 'General Enquiry'), ('product', 'product'), ('sales', 'Sales'), ('other', 'Other')], max_length=15)),
            ],
        ),
    ]
