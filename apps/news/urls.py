from django.conf.urls import patterns, url

from .views import NewsItemListView, NewsItemDetailView


urlpatterns = patterns('',
    url(r'^$', NewsItemListView.as_view(), name='news_newsitem_list'),
    url(r'^(?P<pk>\d+)/$', NewsItemDetailView.as_view(), name='news_newsitem_detail'),
)
