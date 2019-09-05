# coding: utf-8
from datetime import datetime
import csv

from django.shortcuts import redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView


from mailer_recipients import RecipientsMailer

from .models import Event
from .forms import EventOrderForm


class EventDetailView(TemplateView):

    model = Event
    template_name = 'events/event_detail.html'

    def get_queryset(self):
        qs = Event.objects.all()
        qs = qs.filter(is_active=True)
        qs = qs.filter(date_start__lte=datetime.now(), date_stop__gte=datetime.now())
        return qs

    def get_object(self):
        qs = self.get_queryset()
        if qs.exists():
            return qs[0]
        return None

    def get_form(self):
        obj = self.get_object()
        if obj is not None:
            kwargs = {'event_obj': obj}
            if self.request.method == 'POST':
                kwargs.update({'data': self.request.POST})
            form = EventOrderForm(**kwargs)
            return form

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get(self, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            return redirect('/events/close/')
        return super(EventDetailView, self).get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = self.get_form()
        if form.is_valid():
            order = form.save(commit=False)
            order.event = obj
            order.ip = self.get_client_ip(request)
            order.save()
            RecipientsMailer.send(
                request=request,
                object=order,
                template_name='events/mail',
            )
            return redirect('/events/success/')
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'object': self.get_object(),
            'form': self.get_form()
        })
        return super(EventDetailView, self).get_context_data(**kwargs)


def order_export(request, pk=None):
    obj = get_object_or_404(Event, pk=pk)
    user = request.user
    if user.is_authenticated():
        if user.is_superuser:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="event_{}.csv"'.format(obj.pk)
            writer = csv.writer(response, delimiter=';')
            writer.writerow([obj.title.encode('utf-8'), u'', u'', u'', u'', u'', u''])
            writer.writerow([u'ФИО'.encode('utf-8'), u'Компания'.encode('utf-8'), u'Город'.encode('utf-8'), u'Бренд'.encode('utf-8'), u'Телефон'.encode('utf-8'), u'Email'.encode('utf-8'), u'Трансфер'.encode('utf-8'), u'Сообщение'.encode('utf-8'), u'IP'.encode('utf-8')])
            for item in obj.orders.all():
                if item.transfer:
                    transfer = item.transfer.title.encode('utf-8')
                else:
                    transfer = u''.encode(u'utf-8')
                writer.writerow([item.full_name.encode('utf-8'), item.company.encode('utf-8'), item.city.encode('utf-8'), unicode(item.brend).encode('utf-8'), item.phone.encode('utf-8'), item.email.encode('utf-8'), transfer, item.message.encode('utf-8'), unicode(item.ip).encode('utf-8')])
            return response
    raise Http404
