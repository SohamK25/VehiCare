# Generated by Django 5.0.3 on 2024-04-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_alter_attendance_id_alter_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
