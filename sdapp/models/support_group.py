from django.db import models

class SupportGroup(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()
    created_at = models.DateTimeField()
    is_active = models.IntegerField()
    user_view = models.IntegerField()

    class Meta:
        db_table = 'support_group'

# No longer needed