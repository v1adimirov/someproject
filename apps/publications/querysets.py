from django.db.models import Q
from django.db.models import query
from django.utils import timezone
from django.utils.translation import get_language

from publications.models import DatesMixin


class PublicationQuerySet(query.QuerySet):

    def for_site(self, site):
        return self.filter(sites=site)

    def in_language(self, language=None):
        if language is None:
            language = get_language()
        return self.filter(language=language)

    def expired(self):
        return self.filter(expires_at__lt=timezone.now())

    def future(self):
        return self.filter(published_at__gt=timezone.now())

    def enabled(self):
        return self.filter(enabled=True)

    def disabled(self):
        return self.filter(enabled=False)

    def unpublished(self):
        return self.filter(~self._published_q())

    def published(self):
        return self.filter(self._published_q())

    def _published_q(self):
        if issubclass(self.model, DatesMixin):
            now = timezone.now()
            q = Q(expires_at__gte=now) | Q(expires_at=None)
            q &= Q(published_at__lte=now)
            q &= Q(enabled=True)
            return q
        return Q(enabled=True)
