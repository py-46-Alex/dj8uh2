from django_filters import rest_framework as filters, DateFromToRangeFilter
from advertisements.models import Advertisement

# class AdvertisementFilter(FilterSet):
#     """Фильтры для объявлений."""
#
#     status = filters.CharFilter()
#     created_at = filters.DateFromToRangeFilter()
#     updated_at = filters.DateFromToRangeFilter()
#
#     class Meta:
#         model = Advertisement
#         fields = ['status', 'created_at']

# class AdvertisementFilter(filters.FilterSet):
#     """Фильтры для объявлений."""
#     created_at = filters.DateFromToRangeFilter()
#     updated_at = filters.DateFromToRangeFilter()
#     favorite = filters.CharFilter(method='favorites_filter')
#
#     class Meta:
#         model = Advertisement
#         fields = ['status', 'user']
#
#         def favorites_filter(self, queryset, name, value):
#             if value == 'true':
#                 return queryset.filter(favorite=self.request.user)
#             return queryset
        #
class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass
#
class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    status = filters.CharFilter()
    # user = CharFilterInFilter(field_name='user')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']