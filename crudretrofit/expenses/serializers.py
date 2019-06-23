from rest_framework import serializers

from .models import Category, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/17280007/retrieving-a-foreign-key-value-with-django-rest-framework-serializers
    category_name = serializers.ReadOnlyField()
    class Meta:
        model = Expense
        fields = '__all__'
    
    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     print(category_data)
