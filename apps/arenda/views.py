from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import csv

from mailer_recipients import RecipientsMailer

from .forms import OrderForm
from .models import Order


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            message = form.save()
            RecipientsMailer.send(
                request=request,
                object=message,
                template_name='arenda/mail',
            )
            return redirect('arenda_order_success')
    else:
        form = OrderForm()
    return render(request, 'arenda/order_form.html', {
        'form': form,
    })


def order_export(request):
    user = request.user
    if user.is_authenticated():
        if user.is_superuser:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="orders.csv"'
            qs = Order.objects.all()

            writer = csv.writer(response, delimiter=';')
            writer.writerow(map(lambda x: x.verbose_name.encode('utf-8'), Order._meta.fields)[1:])
            for item in qs:
                fields = map(lambda x: x.name, Order._meta.fields)[1:]
                row = map(lambda field: unicode(getattr(item, field)).encode('utf-8'), fields)
                writer.writerow(row)
            return response
    raise Http404
