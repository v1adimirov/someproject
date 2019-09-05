from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .models import NewsItem


class NewsPressMixin(object):

    def get_queryset(self):
        qs = super(NewsPressMixin, self).get_queryset()
        qs = qs.filter(category=self.kwargs.get('news_category'))
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({
            'news_category': self.kwargs.get('news_category'),
            'has_news': NewsItem.objects.filter(category='news').count(),
            'has_press': NewsItem.objects.filter(category='press').count()
        })
        return super(NewsPressMixin, self).get_context_data(**kwargs)


class NewsItemListView(NewsPressMixin, ListView):

    model = NewsItem
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if request.GET.get('page') == '1':
            return redirect(reverse('news_newsitem_list', args=[self.kwargs.get('news_category')]), permanent=True)
        return super(NewsItemListView, self).get(request, *args, **kwargs)


class NewsItemDetailView(NewsPressMixin, DetailView):

    model = NewsItem
