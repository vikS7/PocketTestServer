# Generated by Django 3.0.3 on 2020-10-12 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201010_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Subject'),
        ),
    ]