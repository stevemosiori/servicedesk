# Generated by Django 3.2.4 on 2021-06-27 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sdapp.models.ticket_attachment


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to=sdapp.models.ticket_attachment.get_upload_file_name)),
                ('ticket', models.IntegerField(blank=True, null=True)),
                ('uploaded_ts', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ticket_attachments',
            },
        ),
        migrations.CreateModel(
            name='TicketPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('urgent', 'Urgent')], max_length=191)),
                ('description', models.TextField(blank=True, null=True)),
                ('color_code', models.CharField(blank=True, max_length=191, null=True)),
            ],
            options={
                'db_table': 'ticket_priority',
            },
        ),
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('OPEN', 'Open'), ('PENDING', 'Pending'), ('ANSWERED', 'Answered'), ('RESOLVED', 'Resolved'), ('CLOSED', 'Closed'), ('SPAM', 'Spam')], max_length=191)),
                ('description', models.TextField(blank=True, null=True)),
                ('color_code', models.CharField(blank=True, max_length=191, null=True)),
            ],
            options={
                'db_table': 'ticket_status',
            },
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('support', 'Support'), ('technical', 'Technical'), ('other', 'Other')], max_length=191)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'ticket_type',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=191)),
                ('mailbox_email', models.CharField(blank=True, max_length=191, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('reference_ids', models.TextField(blank=True, null=True)),
                ('is_new', models.IntegerField()),
                ('is_replied', models.IntegerField()),
                ('is_reply_enabled', models.IntegerField()),
                ('is_starred', models.IntegerField()),
                ('is_trashed', models.IntegerField()),
                ('is_agent_viewed', models.IntegerField()),
                ('is_customer_viewed', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_user', to=settings.AUTH_USER_MODEL)),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sdapp.ticketpriority')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sdapp.ticketstatus')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sdapp.tickettype')),
            ],
            options={
                'db_table': 'tickets',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(blank=True, max_length=191, null=True)),
                ('timeformat', models.CharField(blank=True, max_length=191, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(blank=True, max_length=191, null=True)),
                ('timeformat', models.CharField(blank=True, max_length=191, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
