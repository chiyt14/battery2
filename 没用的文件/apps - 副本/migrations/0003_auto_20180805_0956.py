# Generated by Django 2.1 on 2018-08-05 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20180805_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='building_hour_data',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='customer_hour_data',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='device',
            name='building',
        ),
        migrations.RemoveField(
            model_name='device',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='device',
            name='energy_type',
        ),
        migrations.RemoveField(
            model_name='device',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='device',
            name='protocol_type',
        ),
        migrations.RemoveField(
            model_name='device_data',
            name='data_type',
        ),
        migrations.RemoveField(
            model_name='device_data',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='device_hour_data',
            name='sid',
        ),
        migrations.DeleteModel(
            name='Device_p_data',
        ),
        migrations.RemoveField(
            model_name='floor',
            name='building',
        ),
        migrations.RemoveField(
            model_name='floor_hour_data',
            name='sid',
        ),
        migrations.DeleteModel(
            name='Raw_data_lora',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='Building_hour_data',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Customer_hour_data',
        ),
        migrations.DeleteModel(
            name='Data_type',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='Device_data',
        ),
        migrations.DeleteModel(
            name='Device_hour_data',
        ),
        migrations.DeleteModel(
            name='Energy_type',
        ),
        migrations.DeleteModel(
            name='Floor',
        ),
        migrations.DeleteModel(
            name='Floor_hour_data',
        ),
        migrations.DeleteModel(
            name='Protocol',
        ),
    ]
