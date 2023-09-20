from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    filter_data = DateTimeFilter(field_name='dateCreate', lookup_expr='gt', widget=DateTimeInput(
        attrs={'type': 'datetime-local'}))

    class Meta:
        model = Post
        fields = {
            'titlePost': ['icontains'],
            'categoryType': ['exact'],
        }
