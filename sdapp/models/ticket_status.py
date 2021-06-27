from django.db import models

CODE_CHOICES = [
    ('OPEN', 'Open'),
    ('PENDING', 'Pending'),
    ('ANSWERED', 'Answered'),
    ('RESOLVED', 'Resolved'),
    ('CLOSED', 'Closed'),
    ('SPAM', 'Spam'),
]

class TicketStatus(models.Model):
    code = models.CharField(max_length=191, choices=CODE_CHOICES)
    description = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'ticket_status'