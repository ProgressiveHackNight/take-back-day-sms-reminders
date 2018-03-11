# Generated by Django 2.0.3 on 2018-03-11 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertRecipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish')], default='en', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(blank=True, help_text='Type of location (e.g. pharmacy)', max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='alertrecipient',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tbdsms.Location'),
        ),
    ]
