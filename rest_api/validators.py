from rest_framework import serializers


class DateValidate:
    requires_context = True

    def __call__(self, value, serializer):
        if 'from_date' not in value or 'to_date' not in value:
            return
        from_date = value['from_date']
        to_date = value['to_date']

        if from_date >= to_date:
            raise serializers.ValidationError('Start date must be before end date.')


class FreeTimeValidate:
    requires_context = True

    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, value, serializer):
        if 'from_date' not in value or 'to_date' not in value:
            return
        from_date = value['from_date']
        to_date = value['to_date']

        trips = self.queryset.filter(created_by=serializer.context['request'].user)
        from_date_invalid = trips.filter(from_date__lt=from_date, to_date__gt=from_date).count() != 0
        to_date_invalid = trips.filter(from_date__lt=to_date, to_date__gt=to_date).count() != 0
        both_invalid = trips.filter(from_date__gte=from_date, to_date__lte=to_date).count() != 0

        message = 'This date is not free'
        errors = {}
        if from_date_invalid:
            errors['from_date'] = [message, ]
        if to_date_invalid:
            errors['to_date'] = [message, ]
        if both_invalid:
            errors['from_date'] = [message, ]
            errors['to_date'] = [message, ]
        if from_date_invalid or to_date_invalid or both_invalid:
            raise serializers.ValidationError(errors)