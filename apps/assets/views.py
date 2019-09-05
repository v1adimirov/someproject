from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from time import sleep

from django.http import Http404

from mailer import Mailer

from .models import City, VologdaCity, PhotoReport, CityMart
from .forms import (
    FeedbackForm, VologdaFeedbackForm,
    FranchCityFeedbackForm, FranchVologdaFeedbackForm,
    MartFeedbackForm, FranchMartFeedbackForm
)


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            context = {
                'object': message
            }
            if message.city:
                if message.city.has_marts and message.city.city_recipient_email:
                    recipient_email = message.city.city_recipient_email
                else:
                    recipient_email = message.city.recipient_email
                recipients = list(message.city.recipients.all().values_list('email', flat=True))
                if recipient_email:
                    recipients.append(recipient_email)
            else:
                obj = VologdaCity.objects.all()[0]
                recipient_email = obj.recipient_email
                recipients = list(obj.recipients.all().values_list('email', flat=True))
                if recipient_email:
                    recipients.append(recipient_email)
            Mailer.send(
                recipients=recipients,
                context_data=context,
                template_name='assets/mail/feedback',
            )
            return redirect('assets_feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'assets/feedback_form.html', {
        'form': form,
    })


def vologda_feedback_view(request):
    if request.method == 'POST':
        form = VologdaFeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            context = {
                'object': message
            }
            recipient_email = message.mart.recipient_email
            recipients = list(message.mart.recipients.all().values_list('email', flat=True))
            if recipient_email:
                recipients.append(recipient_email)
            Mailer.send(
                recipients=recipients,
                context_data=context,
                template_name='assets/mail/vologda_feedback',
            )
            return redirect('assets_feedback_success')
    else:
        form = VologdaFeedbackForm()
    return render(request, 'assets/vologdafeedback_form.html', {
        'form': form,
    })


def mart_feedback_view(request):
    if request.method == 'POST':
        form = MartFeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            context = {
                'object': message
            }
            recipient_email = message.mart.recipient_email
            recipients = list(message.mart.recipients.all().values_list('email', flat=True))
            if recipient_email:
                recipients.append(recipient_email)
            Mailer.send(
                recipients=recipients,
                context_data=context,
                template_name='assets/mail/mart_feedback',
            )
            return redirect('assets_feedback_success')
    else:
        form = MartFeedbackForm()
    return render(request, 'assets/martfeedback_form.html', {
        'form': form,
    })


def franchcity_feedback_view(request):
    if request.method == 'POST':
        form = FranchCityFeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            context = {
                'object': message
            }
            Mailer.send(
                recipients=[message.franch.recipient_email],
                context_data=context,
                template_name='assets/mail/franchcity_feedback',
            )
            return redirect('assets_feedback_success')
    else:
        form = FranchCityFeedbackForm()
    return render(request, 'assets/franchcityfeedback_form.html', {
        'form': form,
    })


def franchvologda_feedback_view(request):
    if request.method == 'POST':
        form = FranchVologdaFeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            context = {
                'object': message
            }
            Mailer.send(
                recipients=[message.franch.recipient_email],
                context_data=context,
                template_name='assets/mail/franchvologda_feedback',
            )
            return redirect('assets_feedback_success')
    else:
        form = FranchVologdaFeedbackForm()
    return render(request, 'assets/franchvologdafeedback_form.html', {
        'form': form,
    })


def franchmart_feedback_view(request):
    if request.method == 'POST':
        form = FranchMartFeedbackForm(request.POST)
        if form.is_valid():
            message = form.save()
            context = {
                'object': message
            }
            Mailer.send(
                recipients=[message.franch.recipient_email],
                context_data=context,
                template_name='assets/mail/franchmart_feedback',
            )
            return redirect('assets_feedback_success')
    else:
        form = FranchMartFeedbackForm()
    return render(request, 'assets/franchmartfeedback_form.html', {
        'form': form,
    })


class CityDetailView(DetailView):

    queryset = City.objects.filter(is_active=True)


class CityDetaiWithMartsView(ListView):

    model = CityMart
    template_name = 'assets/city_with_marts.html'

    def get_city(self):
        city_slug = self.kwargs.get('city_slug')
        return get_object_or_404(City, slug=city_slug)

    def get_queryset(self):
        qs = super(CityDetaiWithMartsView, self).get_queryset()
        city = self.get_city()
        qs = qs.filter(city=city)
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({'city': self.get_city()})
        return super(CityDetaiWithMartsView, self).get_context_data(**kwargs)


class FranchMartView(DetailView):

    model = CityMart
    template_name = 'assets/franch_mart.html'

    def get_city(self):
        city_slug = self.kwargs.get('city_slug')
        return get_object_or_404(City, slug=city_slug)

    def get_queryset(self):
        qs = super(FranchMartView, self).get_queryset()
        city = self.get_city()
        qs = qs.filter(city=city)
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({'city': self.get_city()})
        return super(FranchMartView, self).get_context_data(**kwargs)


def vologda_page(request):
    try:
        obj = VologdaCity.objects.all()[0]
    except IndexError:
        raise Http404
    return render(
        request, 'assets/vologda.html', {
            'object': obj
    })


class PhotoReportListView(ListView):

    model = PhotoReport
    paginate_by = 9

    def get(self, request, *args, **kwargs):
        if request.GET.get('page') == '1':
            return redirect(reverse('assets_photoreport_list', args=[self.get_city().pk]), permanent=True)
        return super(PhotoReportListView, self).get(request, *args, **kwargs)

    def get_city(self):
        pk = self.kwargs.get('city_id')
        return get_object_or_404(City, pk=pk)

    def get_queryset(self):
        qs = super(PhotoReportListView, self).get_queryset()
        qs = qs.filter(city=self.get_city())
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({
            'city': self.get_city(),
        })
        return super(PhotoReportListView, self).get_context_data(**kwargs)


class PhotoReportDetailView(DetailView):

    model = PhotoReport

    def get_city(self):
        pk = self.kwargs.get('city_id')
        return get_object_or_404(City, pk=pk)

    def get_queryset(self):
        qs = super(PhotoReportDetailView, self).get_queryset()
        qs = qs.filter(city=self.get_city())
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({
            'city': self.get_city(),
        })
        return super(PhotoReportDetailView, self).get_context_data(**kwargs)
