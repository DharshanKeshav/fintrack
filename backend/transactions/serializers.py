from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'color']

class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            'id', 'category', 'category_name',
            'amount', 'type', 'description', 'date', 'created_at'
        ]
        read_only_fields = ['created_at']