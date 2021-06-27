from django.db import models

class SupportTeam(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()
    created_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        db_table = 'support_team'

# No longer needed