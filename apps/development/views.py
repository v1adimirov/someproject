from django.shortcuts import render, redirect
from django.http import Http404
from mailer_recipients import RecipientsMailer

from .models import DevelpmentPage
from .forms import OrderForm


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            message = form.save()
            RecipientsMailer.send(
                request=request,
                object=message,
                template_name='development/mail',
            )
            return redirect('development_order_success')
    else:
        form = OrderForm()
    return render(request, 'development/order_form.html', {
        'form': form,
    })


def development_page(request):
    try:
        obj = DevelpmentPage.objects.all()[0]
    except IndexError:
        raise Http404
    return render(
        request, 'development/development.html', {
            'object': obj
    })


