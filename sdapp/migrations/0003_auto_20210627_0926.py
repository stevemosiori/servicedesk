# Generated by Django 3.2.4 on 2021-06-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdapp', '0002_auto_20210627_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='is_trashed',
        ),
        migrations.AddField(
            model_name='ticket',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_agent_viewed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_customer_viewed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_new',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_replied',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_reply_enabled',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_starred',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]