import django_filters
from .models import Snippet


class SnippetFilter(django_filters.FilterSet):

    class Meta:
        model = Snippet
        fields = ('title', 'body', 'created')
