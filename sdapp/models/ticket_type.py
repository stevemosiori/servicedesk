from django.db import models

TICKET_TYPES = [
    ('support', 'Support'),
    ('technical', 'Technical'),
    ('other', 'Other'),
]

class TicketType(models.Model):
    code = models.CharField(max_length=191, choices=TICKET_TYPES)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        db_table = 'ticket_type'