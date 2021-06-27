# Generated by Django 3.2.4 on 2021-06-27 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sdapp.appuser'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sdapp.customer'),
        ),
    ]