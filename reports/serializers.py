from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')

    class Meta:
        model = Report
        fields = [
            'id',
            'reporter',
            'note',
            'reason',
            'description',
            'created_at',
        ]