# Generated by Django 3.1.4 on 2021-04-15 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_auto_20210321_1224'),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vendors', models.ManyToManyField(related_name='orders', to='vendors.Vendor')),
            ],
            options={
                'ordering': ['-cree_le'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_paid', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendors.vendor')),
            ],
        ),
    ]
