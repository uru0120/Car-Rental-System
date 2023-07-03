# Generated by Django 4.1.7 on 2023-06-16 12:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('capacity', models.CharField(max_length=2)),
                ('is_available', models.BooleanField(default=True)),
                ('rent', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CarDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('earings', models.IntegerField(default=0)),
                ('type', models.CharField(blank=True, max_length=20)),
                ('car_dealer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.CharField(max_length=10)),
                ('days', models.CharField(max_length=3)),
                ('is_complete', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.car')),
                ('car_dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cardealer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('type', models.CharField(blank=True, max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cardealer',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='home.location'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.cardealer'),
        ),
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.location'),
        ),
    ]
