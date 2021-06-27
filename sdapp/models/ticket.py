from django.db import models
from .ticket_status import TicketStatus
from .ticket_priority import TicketPriority
from .ticket_type import TicketType
from .user import AppUser, Customer

class Ticket(models.Model):
    status = models.ForeignKey(TicketStatus, on_delete=models.DO_NOTHING, blank=True, null=True)
    priority = models.ForeignKey(TicketPriority, on_delete=models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(TicketType, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    agent = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    source = models.CharField(max_length=191)
    subject = models.CharField(max_length=191)
    message = models.TextField(blank=True, null=True)
    reference_ids = models.TextField(blank=True, null=True)
    is_new = models.IntegerField(default=1)
    is_replied = models.IntegerField(default=0)
    is_reply_enabled = models.IntegerField(default=1)
    is_starred = models.IntegerField(default=0)
    is_agent_viewed = models.IntegerField(default=0)
    is_customer_viewed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tickets'