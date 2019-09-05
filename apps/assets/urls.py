from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView
from .views import (
    CityDetailView, feedback_view, vologda_feedback_view,
    vologda_page, PhotoReportListView, PhotoReportDetailView,
    franchcity_feedback_view, franchvologda_feedback_view,
    CityDetaiWithMartsView, mart_feedback_view, CityMart,
    FranchMartView, franchmart_feedback_view
)

from .models import City, VologdaMart


urlpatterns = patterns('',
    url(r'^vologda/$', vologda_page, name='assets_vologda'),
    url(r'^vologda/(?P<pk>\d+)/franchise/$', DetailView.as_view(model=VologdaMart, template_name='assets/franch_vologda.html'), name='assets_franchvologda_list'),
    url(r'^vologda/feedback/$', vologda_feedback_view, name='assets_vologda_feedback_form'),
    url(r'^franchcity/feedback/$', franchcity_feedback_view, name='assets_franchcity_feedback_form'),
    url(r'^franchvologda/feedback/$', franchvologda_feedback_view, name='assets_franchvologda_feedback_form'),
    url(r'^franchmart/feedback/$', franchmart_feedback_view, name='assets_franchmart_feedback_form'),
    url(r'^mart/feedback/$', mart_feedback_view, name='assets_mart_feedback_form'),
    url(r'^feedback/$', feedback_view, name='assets_feedback_form'),
    url(r'^feedback/success/$', TemplateView.as_view(
            template_name='assets/feedback_success.html'
        ), name='assets_feedback_success'),
    url(r'^photoreports/(?P<city_id>\d+)/$', PhotoReportListView.as_view(), name='assets_photoreport_list'),
    url(r'^photoreports/(?P<city_id>\d+)/(?P<pk>\d+)/$', PhotoReportDetailView.as_view(), name='assets_photoreport_detail'),

    url(r'^city/(?P<city_slug>[\w\-]+)/$', CityDetaiWithMartsView.as_view(), name='assets_city_marts_list'),
    url(r'^city/(?P<city_slug>[\w\-]+)/(?P<pk>\d+)/franchise/$', FranchMartView.as_view(template_name='assets/franch_mart.html'), name='assets_franchmart_list'),

    url(r'^(?P<slug>[\w\-]+)/$', CityDetailView.as_view(), name='assets_city_detail'),
    url(r'^(?P<slug>[\w\-]+)/video/$', DetailView.as_view(model=City, template_name='assets/video.html'), name='assets_camera_list'),
    url(r'^(?P<slug>[\w\-]+)/franchise/$', DetailView.as_view(model=City, template_name='assets/franch.html'), name='assets_franch_list'),
)
