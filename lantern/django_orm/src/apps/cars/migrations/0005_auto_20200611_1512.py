# Generated by Django 3.0.6 on 2020-06-11 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20200611_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('sold', 'Sold'), ('archived', 'Archived')], default='pending', max_length=15)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['status'], name='cars_order_status_a1b093_idx'),
        ),
    ]
