# Generated by Django 3.1.7 on 2021-10-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docuser',
            name='otp',
            field=models.BooleanField(default=False),
        ),
    ]
