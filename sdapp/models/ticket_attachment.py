import os
import hashlib
import time
from django.db import models
from .ticket import Ticket

def get_upload_file_name(instance, filename):
    fname, ext = os.path.splitext(filename)
    ts = time.time()
    return 'public/uploads/attachments/' + '{ts}'.format(ts=ts) + hashlib.sha1(instance.file.read()).hexdigest() + ext

class TicketAttachment(models.Model):
    name = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=get_upload_file_name)
    ticket = models.IntegerField(null=True, blank=True)
    uploaded_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ticket_attachments'