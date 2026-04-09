from rest_framework import serializers
from .models import Budget, Goal

class BudgetSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True
    )

    class Meta:
        model = Budget
        fields = [
            'id', 'category', 'category_name',
            'limit_amount', 'month', 'year'
        ]


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'id', 'title', 'target_amount',
            'current_amount', 'deadline', 'created_at'
        ]
        read_only_fields = ['created_at']