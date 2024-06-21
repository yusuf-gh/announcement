import django_filters
from .models import User


class UserFilterByAge(django_filters.FilterSet):
    max_age = django_filters.NumberFilter(method="filter_by_age")
    
    class Meta:
        model = User
        fields = []
        
    def filter_by_age(self, queryset, name, value):
        from datetime import date
        
        today = date.today()
        threshold_date = today.replace(year=today.year - int(str(value)))
        return queryset.filter(date_of_birth__gte=threshold_date)