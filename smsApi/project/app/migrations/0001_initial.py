# Generated by Django 4.2.8 on 2024-01-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='off', max_length=3)),
            ],
        ),
    ]