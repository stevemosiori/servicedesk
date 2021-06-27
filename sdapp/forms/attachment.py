from sdapp.models.ticket_attachment import TicketAttachment
from django.forms import ModelForm

class AttachmentForm(ModelForm):
    class Meta:
        model = TicketAttachment
        fields = ['name', 'content_type', 'file']