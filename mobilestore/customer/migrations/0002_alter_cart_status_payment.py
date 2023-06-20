# Generated by Django 4.1.7 on 2023-03-28 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_alter_product_battery_alter_product_ram_and_more'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='carted', max_length=100),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100)),
                ('acholdername', models.CharField(max_length=100)),
                ('accno', models.IntegerField()),
                ('ifsc', models.CharField(max_length=100, null=True)),
                ('quantity', models.PositiveBigIntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_payment', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_paayment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]