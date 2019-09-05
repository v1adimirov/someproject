from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils import timezone
from django.utils.translation import get_language, ugettext_lazy as _


LANGUAGES = tuple((code, _(name)) for code, name in settings.LANGUAGES)


class MultisiteMixin(models.Model):

    sites = models.ManyToManyField(
        to=Site,
        verbose_name=_('sites'),
        related_name='%(app_label)s_%(class)s_set',
    )

    class Meta:
        abstract = True


class MultilingualMixin(models.Model):

    language = models.CharField(
        verbose_name=_('language'),
        max_length=255,
        choices=LANGUAGES,
        default=get_language,
    )

    class Meta:
        abstract = True


class WeightMixin(models.Model):

    weight = models.PositiveIntegerField(
        verbose_name=_('weight'),
        default=100,
    )

    class Meta:
        abstract = True


class DatesMixin(models.Model):

    published_at = models.DateTimeField(
        verbose_name=_('published at'),
        default=timezone.now,
        help_text=_(
            'Publication will be visible to visitors starting from this date.'
        ),
    )
    expires_at = models.DateTimeField(
        verbose_name=_('expires at'),
        null=True,
        blank=True,
        help_text=_(
            'Publication will be visible to visitors due to this date if set.'
        ),
    )

    class Meta:
        abstract = True


from .querysets import PublicationQuerySet


class Publication(models.Model):
    """This abstract model provides publication-specific fields and tools."""

    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True,
        help_text=_('If not set, publication is hidden from visitors anyway.'),
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )

    objects = PublicationQuerySet.as_manager()

    class Meta:
        abstract = True
