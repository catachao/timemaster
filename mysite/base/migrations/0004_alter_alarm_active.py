# Generated by Django 5.0 on 2024-07-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_alarm_options_alarm_created_alarm_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]