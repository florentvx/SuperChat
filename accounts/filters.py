import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ChatFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="DateCreated",
                            lookup_expr="gte",
                            label="date from",
                            input_formats=['%d/%m/%Y'])
    less_date = DateFilter(field_name="DateCreated",
                           lookup_expr="lte",
                           label="date to",
                           input_formats=['%d/%m/%Y'],
                           )
    name_search = CharFilter(field_name='Name', lookup_expr='icontains', label="Name")

    class Meta:
        model = Chat
        fields = ['Host']
        # filter_overrides = {
        #     models.DateTimeField: {
        #         'filter_class': django_filters.DateFilter,
        #          'extra': lambda f: {
        #              'widget': AdminDateInput
        #          },
        #     }
        # }
