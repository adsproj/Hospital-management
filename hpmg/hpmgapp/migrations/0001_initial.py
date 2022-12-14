# Generated by Django 4.0.5 on 2022-07-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('age', models.TextField()),
                ('gender', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField()),
                ('department', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
    ]
