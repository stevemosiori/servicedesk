from django.db import models

TICKET_PRIORITIES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('urgent', 'Urgent'),
]

class TicketPriority(models.Model):
    code = models.CharField(max_length=191, choices=TICKET_PRIORITIES)
    description = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'ticket_priority'