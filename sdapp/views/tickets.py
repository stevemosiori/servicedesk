from django.http.response import JsonResponse
from sdapp.models import TicketAttachment, TicketStatus, TicketPriority, TicketType
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from upload_validator import FileTypeValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from sdapp.models import AppUser, Customer, Ticket

@login_required
@csrf_exempt
@require_http_methods(["GET", "POST"])
def tickets(request):
    if request.method == 'GET':
        return render(request, 'sdapp/tickets/index.html', {
            'view_reqs': ['datatables']
        })
    elif request.method == 'POST':
        output = {}

        dt_config = process_dt_params(request)

        output['draw'] = dt_config['draw']
        output['recordsTotal'] = 40
        output['recordsFiltered'] = 80
        output['data'] = []

        all_tickets = Ticket.objects.all()

        dt_data = []
        count = dt_config['start']
        for ticket in all_tickets:
            dt_data.append(
                """
                
                """
            )

        return JsonResponse(output)

def process_dt_params(request):
    data = request.POST
    
    return {
        'search': data.get('search[value]', ''),
        'start': data.get('start', 0),
        'draw': data.get('draw', 1),
        'length': data.get('length', 20),
        'order_dir': data.get('order[0][dir]', 'desc'),
        'order': data.get('order[0][column]', 0)
    }

@login_required
@csrf_exempt
def new_ticket(request):
    if request.method == 'GET':
        # Reset the attachment list for new tickets
        if 'ticket_attachments' in request.session:
            request.session['ticket_attachments'] = []

        return render(request, 'sdapp/tickets/new_ticket.html', {
            'view_reqs': ['summernote', 'dropzone', 'jquery_form']
        })
    elif request.method == 'POST':
        try:
            data = request.POST

            ticketStatus = TicketStatus.objects.get(code="PENDING")
            ticketPriority = TicketPriority.objects.get(code=data['ticketPriority'])
            ticketType = TicketType.objects.get(code=data['ticketType'])
            customerFirstName = data['customerFirstName']
            customerLastName = data['customerLastName']
            ticketSource = data['ticketSource']
            customerEmail = data['customerEmail']
            ticketSubject = data['ticketSubject']
            ticketMessage = data['ticketMessage']

            customer_user = None
            customer_user_filter = User.objects.filter(email=customerEmail)
            if customer_user_filter.count() > 0:
                customer_user = User.objects.get(email=customerEmail)
            else:
                customer_user = User.objects.create_user(customerEmail, customerEmail, 'changeme')
                customer_user.first_name = customerFirstName
                customer_user.last_name = customerLastName
                customer_user.save()

            customer = None
            customer_filter = Customer.objects.filter(user=customer_user)
            if customer_filter.count() > 0:
                customer = Customer.objects.get(user=customer_user)
            else:
                customer = Customer(
                    user=customer_user
                )

                customer.save()

            agent = request.user
            agent = AppUser.objects.get(user=agent)

            ticket = Ticket(
                status = ticketStatus,
                priority = ticketPriority,
                type = ticketType,
                customer = customer,
                agent = agent,
                source = ticketSource,
                subject = ticketSubject,
                message = ticketMessage
            )

            ticket.save()

            # Attach the attachments, yes we are attaching the attachments
            if 'ticket_attachments' in request.session:
                current_attachments = request.session['ticket_attachments']

                for attachment in current_attachments:
                    saved_attachment = TicketAttachment.objects.get(pk=attachment)
                    saved_attachment.ticket = ticket.id
                    saved_attachment.save()

                # We no longer require it
                del request.session['ticket_attachments']

            return JsonResponse({
                'message': 'success',
                'reason': 'Ticket added successfully'
            })
        except Exception as e:
            return JsonResponse({
                'message': 'error',
                'reason': e.__str__()
            })

@login_required
@csrf_exempt
def upload_attachment(request):
    if request.method == 'POST':
        attachment = request.FILES['ticketAttachment']
        try:
            validator = FileTypeValidator(
                allowed_types=[
                    'image/png',
                    'application/pdf',
                    'application/msword',
                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    'image/jpeg',
                    'application/zip',
                ],
                allowed_extensions=['.png', '.pdf', '.doc', '.docx', '.jpeg', '.jpg', '.zip']
            )
            validator(attachment)

            model = TicketAttachment(name=attachment.name, file=attachment)
            model.save()

            if 'ticket_attachments' in request.session:
                current_attachments = request.session['ticket_attachments']
                current_attachments.append(model.id)

                request.session['ticket_attachments'] = current_attachments
            else:
                request.session['ticket_attachments'] = [model.id]

            return HttpResponse(repr(request.session.items()))
        except ValidationError as e: 
            res = HttpResponse(e.messages)
            res.status_code = 400
            return res

        # return HttpResponse(repr(model))