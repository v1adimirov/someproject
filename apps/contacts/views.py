from django.views.generic import ListView
from django.shortcuts import render, redirect

from mailer_recipients import RecipientsMailer

from .models import Person
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            RecipientsMailer.send(
                request=request,
                object=message,
                template_name='contacts/mail',
            )
            return redirect('contacts_feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'contacts/feedback_form.html', {
        'form': form,
    })


class PersonListView(ListView):

    queryset = Person.objects.filter(is_active=True)
    model = Person
